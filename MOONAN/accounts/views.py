from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib.auth import get_user_model
from users.models import User, Connection

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

def connection_view(request):
    if request.method=='POST':
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
                existing_connection = Connection.objects.filter(from_user=from_user, to_user=to_user)
                if existing_connection.exists():
                    error_message = '이미 연결 신청을 하셨습니다.'
                    return render(request, 'connection.html', {'error_message': error_message})
                
                connection = Connection.objects.create(
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
    
def logout_view(request):
    # 로그인일 때 데이터 유효성 검사
    if request.user.is_authenticated:
        # 로그아웃 로직 처리
        logout(request)
        # 리다이렉트
        return redirect('accounts:login')