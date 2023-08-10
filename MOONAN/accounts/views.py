from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib.auth import get_user_model
from users.models import User, Connection, ConnectionRequest
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Medication, Nutrition
from users.models import UserMedication, UserNutrition
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.db.models import Q


User = get_user_model()

def join_view(request):
    # POST 요청할 경우
    if request.method == 'POST':
        name = request.POST.get('name')
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        password_check = request.POST.get('password-repeat')
        
        # 필드값을 입력하지 않을 경우
        if not name or not user_id or not password or not password_check:
            error_message = '모든 필드를 입력해주세요.'
            return render(request, 'accounts/join.html', {'error_message': error_message})
        
        # 데이터 저장
        user = User.objects.create_user(name=name, user_id=user_id, password=password)
        user.save()

        # 리다이렉트
        return redirect('accounts:login') 
    
    # GET 요청할 경우, 회원가입 HTML 응답
    return render(request, 'accounts/join.html')

@csrf_exempt
def id_check(request): # 아이디 중복 체크 목적
    if request.method == 'POST':
        user_id = request.POST.get('user_id', '')
        try:
            user = User.objects.get(user_id=user_id)
            result = {
                'result': 'success',
                'data': 'exist'
            }
        except ObjectDoesNotExist:
            result = {
                'result': 'success',
                'data': 'not exist'
            }

        return JsonResponse(result)

def login_view(request):
    # POST 요청할 경우
    if request.method == 'POST':
        user_id = request.POST.get('name')
        password = request.POST.get('password')

        # 사용자 인증
        user = authenticate(request, user_id=user_id, password=password)

        if user is not None:
            # 사용자 인증 성공 시 로그인
            login(request, user)

            if not request.POST.get('saveLogin'):
            # "로그인 정보 저장하기" 체크박스가 선택되지 않은 경우, 세션 만료 시간을 브라우저 종료 시점으로 설정
                request.session.set_expiry(0)
            else:
            # "로그인 정보 저장하기" 체크박스가 선택된 경우, settings에서 설정한 만료 시간으로 설정
                request.session.set_expiry(settings.SESSION_COOKIE_AGE)
            # 리다이렉트
            return redirect('accounts:connection')
        else:
            # 사용자 인증 실패 시 에러 처리
            user_exists = User.objects.filter(user_id=user_id).exists()
            if not user_exists:
                error_message = '잘못된 아이디입니다.'
                return render(request, 'accounts/login.html', {'error_message': error_message})
            else:
                error_message = '잘못된 비밀번호입니다.'
        
            return render(request, 'accounts/login.html', {'error_message': error_message, 'user_id': user_id})
    
    # GET 요청할 경우, 로그인 HTML 응답
    return render(request, 'accounts/login.html')

@login_required
def send_connection_request(request):
    if request.method =='POST':
        from_user = request.user
        to_user = request.POST.get('to_user')
        relationship1 = request.POST.get('relationship1')
        relationship2 = request.POST.get('relationship2')
        
        try:
            to_user = get_user_model().objects.get(name=to_user)
        except get_user_model().DoesNotExist:
            # 사용자를 찾을 수 없는 경우에 대한 처리
            error_message = '사용자를 찾을 수 없습니다.'
            return render(request, 'connection.html', {'error_message': error_message})
        else:
                # 중복 신청 검사
                existing_connection = ConnectionRequest.objects.filter(
                Q(from_user=from_user, to_user=to_user) | Q(from_user=to_user, to_user=from_user)
                )
                if existing_connection.exists():
                    error_message = '이미 연결 신청을 하셨습니다.'
                    return render(request, 'connection.html', {'error_message': error_message})
                
                connection_request = ConnectionRequest.objects.create(
                    from_user=from_user,
                    to_user=to_user,
                    relationship1=relationship1,
                    relationship2=relationship2,
                )
                # 필요한 후속 처리 (예: 연결 완료 메시지 표시)
                return redirect('main')  # 또는 적절한 리다이렉트 경로 설정
    else:
        # return render(request, 'accounts/accountConnection.html')
        return render (request, 'connection.html')
    
@login_required
def info_view(request):
    user = request.user
    if request.method =='POST':
        user_id = request.user.user_id  # 현재 로그인한 사용자의 아이디
        birthdate_str = request.POST.get("birthdate")
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()

        gender = request.POST.get("gender")
        med_or_nutr_status = request.POST.get("med_or_nutr_status") 
        medications = request.POST.getlist("medication")
        nutritions = request.POST.getlist("nutrition")

        # 사용자 추가 정보 업데이트
        user = get_object_or_404(User, user_id=user_id)  # 아이디로 유저를 찾아옴
        user.birthdate = birthdate
        user.gender = gender
        user.med_or_nutr_status = med_or_nutr_status
        user.save()

        # 기존에 연결된 데이터를 제거하고 사용자가 선택한 약과 영양제 정보를 저장
        user.medications.clear()
        user.nutritions.clear()
        

        # 사용자가 선택한 약 정보를 추가
        for medication_name in medications:
            medication, _ = Medication.objects.get_or_create(medication_name=medication_name) # medication_name을 Medication 모델에서 약을 찾거나 없으면 생성
            # 앞에서 찾거나 생성된 medication을 UserMedication 모델에서 또 다시 찾거나 없으면 생성
            user_medication, created = UserMedication.objects.get_or_create(user=user, medication=medication) 
            if created:
                user.medications.add(medication)  # Medication 인스턴스를 추가, UserMedication 인스턴스를 추가하지 않도록 주의

        for nutrition_name in nutritions:
            nutrition, _ = Nutrition.objects.get_or_create(nutrition_name=nutrition_name) 
            user_nutrition, created = UserNutrition.objects.get_or_create(user=user, nutrition=nutrition)
            if created:
                user.nutritions.add(nutrition)

        return redirect('main')

    context = {
        'medication_choices': Medication.MEDICATION_CHOICES,
        'nutrition_choices': Nutrition.NUTRITION_CHOICES,
    }
    return render(request, 'accounts/info.html', context)

# 사용자가 직접 복용하는 약 추가
def add_medication(request): 
    new_medication = request.POST.get("new_medication")
    
    # 데이터베이스에 저장
    if new_medication:
        medication, created = Medication.objects.get_or_create(medication_name=new_medication)
        
    # 선택지 목록 업데이트
    medication_choices = list(Medication.MEDICATION_CHOICES)  # 기존 선택지
    medication_choices.append((medication.medication_name, medication.medication_name))  # 새로운 선택지
    response_data = {
        "medication_list": [{"label": label, "value": value} for value, label in medication_choices]
    }
    return JsonResponse(response_data)

# 사용자가 직접 복용하는 영양제 추가
def add_nutrition(request): 
    new_nutrition = request.POST.get("new_nutrition")
    
    # 데이터베이스에 저장
    if new_nutrition:
        nutrition, created = Nutrition.objects.get_or_create(nutrition_name=new_nutrition)
        
    # 선택지 목록 업데이트
    nutrition_choices = list(Nutrition.NUTRITION_CHOICES)  # 기존 선택지
    nutrition_choices.append((nutrition.nutrition_name, nutrition.nutrition_name))  # 새로운 선택지
    response_data = {
        "nutrition_list": [{"label": label, "value": value} for value, label in nutrition_choices]
    }
    return JsonResponse(response_data)
    
def logout_view(request):
    # 로그인일 때 데이터 유효성 검사
    if request.user.is_authenticated:
        # 로그아웃 로직 처리
        logout(request)
        # 리다이렉트
        return redirect('accounts:login')