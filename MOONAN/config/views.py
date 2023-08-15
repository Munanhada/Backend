from django.views.generic import TemplateView
from users.models import User, Connection, ConnectionRequest
from message.models import Message
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
import json
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from users.models import UserMedication, UserNutrition

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')  # 로그인 페이지로 리디렉션

    user = request.user

    # 오늘 받은 메시지 
    today = timezone.now().date()  # 오늘 날짜
    received_messages = Message.objects.filter(receiver=request.user, timestamp__date=today)


    # 연결 중인 계정과 관계 정보
    connected_users = Connection.objects.filter(Q(user1=user) | Q(user2=user))
    connected_users_with_relationship = []

    # user1-user2 mother-daughter이면 user1에게 user2는 daughter 처리
    for connected_user in connected_users:
        if connected_user.user1 == user:
            relationship = connected_user.relationship2
            other_user = connected_user.user2
        else:
            relationship = connected_user.relationship1
            other_user = connected_user.user1
            
        connected_users_with_relationship.append({
            'other_user': other_user,
            'relationship': relationship,  
        })
    
    # 추천 문안인사 선택지 
    recommendContent_choices = Message.RECOMMENDCONTENT_CHOICES

    # 사용자가 복용하는 약 및 영양제 목록 불러오기
    user_medications = UserMedication.objects.filter(user=request.user)
    user_nutritions = UserNutrition.objects.filter(user=request.user)

    context = {
        'user': user,
        'received_messages' : received_messages,
        'recommendContent_choices': recommendContent_choices,
        'connected_users': connected_users_with_relationship,
        'user_medications': user_medications,
        'user_nutritions': user_nutritions,
    }

    return render(request, 'home.html', context)

# 문안인사 메시지 보내기
@login_required
def send_message(request):
    if request.method == 'POST':
        receiver_id = request.POST.get('receiver_id')
        recommendContent = request.POST.get('recommendContent')
        customContent = request.POST.get('customContent')
        
        # 오류 처리 
        if not receiver_id:
            response_data = {
                'success': False,
                'message': '수신자를 선택해주세요.',
            }
            return JsonResponse(response_data, status=400)
        if not recommendContent and not customContent:
            response_data = {
                'success': False,
                'message': '메시지 내용을 입력해주세요.',
            }
            return JsonResponse(response_data, status=400)
        try:
            receiver = User.objects.get(id=receiver_id)
            sender = request.user
            Message.objects.create(
                sender=sender,
                receiver=receiver,
                recommendContent=recommendContent,
                customContent=customContent,
            )
            response_data = {
                'success': True,
                'message': '문안인사가 성공적으로 전송되었습니다!',
            }
            return JsonResponse(response_data)
        except User.DoesNotExist:
            response_data = {
                'success': False,
                'message': '수신자를 찾을 수 없습니다.',
            }
            return JsonResponse(response_data, status=400)
    

# 연결 요청 수락 - ConnetionRequest.is_accepted true, Connection 생성, json 형식으로 전달
def accept_connection_request(request):
    user = request.user

    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        connection_request = ConnectionRequest.objects.get(id=request_id)
        
        connection_request.is_accepted=True
        connection_request.save()  # 수정 내용을 데이터베이스에 저장

        # Connection 테이블에 정보 복사
        Connection.objects.create(
            user1=connection_request.from_user,
            user2=connection_request.to_user,
            relationship1=connection_request.relationship1,
            relationship2=connection_request.relationship2,
            is_accepted=True,
        )
        
        # ConnectionRequest 테이블에서 데이터 삭제 -> 일단 추적해보자 
        # connection_request.delete()
        
        # 연결 요청받은 정보
        connection_requests_received = ConnectionRequest.objects.filter(to_user=user, is_accepted=False)
        # QuerySet을 리스트로 변환하고, 각 요소를 딕셔너리로 변환
        connection_requests_received_list = []
        for request in connection_requests_received:
            connection_requests_received_list.append({
                'request_id': request.pk,
                'from_user_name': request.from_user.name,
                'relationship2': request.relationship2,
            })
        
        # 연결된 계정 정보 새로 가져오기
        connected_users = Connection.objects.filter(Q(user1=user) | Q(user2=user)) 
        connected_users_with_relationship = []

        # user1-user2 mother-daughter이면 user1에게 user2는 daughter 처리
        for connected_user in connected_users:
            if connected_user.user1 == user:
                relationship = connected_user.relationship2
                other_user_name = connected_user.user2.name
            else:
                relationship = connected_user.relationship1
                other_user_name = connected_user.user1.name
            
            connected_users_with_relationship.append({
                'other_user_name': other_user_name,
                'relationship': relationship,  
            })
        
        response_data = {
            'success': True,
            'message': '수락 요청이 수락되었습니다.',
            'connected_users': connected_users_with_relationship,
            'connection_requests_received': connection_requests_received_list,
        }
        print(response_data)
        return JsonResponse(response_data)

# 연결 요청 거절
def reject_connection_request(request):
    user = request.user

    request_id = request.POST.get('request_id')
    connection_request = ConnectionRequest.objects.get(id=request_id)
    
    # 해당 연결요청 삭제
    connection_request.delete()

    # 연결 요청받은 정보
    connection_requests_received = ConnectionRequest.objects.filter(to_user=user, is_accepted=False)
    # QuerySet을 리스트로 변환하고, 각 요소를 딕셔너리로 변환
    connection_requests_received_list = []
    for request in connection_requests_received:
        connection_requests_received_list.append({
            'request_id': request.pk,
            'from_user_name': request.from_user.name,
            'relationship2': request.relationship2,
        })
    response_data = {
        'success': True,
        'message': '거절 요청이 수락되었습니다.',
        'connection_requests_received': connection_requests_received_list,
    }
    print(response_data)
    return JsonResponse(response_data)
        
# home/alarm
# 연결 요청중, 요청 받음, 메시지 받음 
def alarm_view(request):
    if request.method == 'POST':
        pass
    
    if not request.user.is_authenticated:
        return redirect('accounts:login')  # 로그인 페이지로 리디렉션

    user = request.user
    # 연결 요청 중인 경우
    connection_requests = ConnectionRequest.objects.filter(from_user=user, is_accepted=False)
    
    # 연결 요청을 받은 경우
    connection_requests_received = ConnectionRequest.objects.filter(to_user=user, is_accepted=False)
    
    today = timezone.now().date()  # 오늘 날짜
    last_week_start = today - timedelta(days=today.weekday() + 7)  # 이번주 첫째 날
    last_month_start = today.replace(day=1) - timedelta(days=1)  # 이번달 첫째 날의 이전 날
    
    # 오늘 받은 메시지 
    received_todayMessages = Message.objects.filter(receiver=request.user, timestamp__date=today)
    
    # 이번주 중 오늘을 제외한 메시지
    received_last_week_messages = Message.objects.filter(receiver=request.user, timestamp__date__range=(last_week_start, today - timedelta(days=1)))

    # 이번달 중 오늘을 제외한 메시지
    received_last_month_messages = Message.objects.filter(receiver=request.user, timestamp__date__range=(last_month_start, today - timedelta(days=1)))

    context = {
        'user': user,
        'connection_requests' : connection_requests,
        'connection_requests_received': connection_requests_received,
        'received_todayMessages': received_todayMessages,
        'received_last_week_messages' : received_last_week_messages,
        'received_last_month_messages' : received_last_month_messages,
    }
    return render(request, 'alarm.html', context)

# 약/영양제 먹었는지, 운동했는지 상태 업데이트
def daily_status(request):
    user = request.user
    if request.method == 'POST':
        status_type = request.POST.get("actionType")
        status_value = request.POST.get("status")

        if status_type == 'medication':
            user.has_medication_or_nutrition = (status_value == 'true')
        elif status_type == 'exercise':
            user.has_exercised = (status_value == 'true')
        
        user.save()
                
        return JsonResponse({'status': 'success'})
        
    return JsonResponse({'status': 'error', 'message': '요청 실패'})


# 약/영양제 먹었는지, 운동했는지 상태 초기화
def reset_daily_status(request):
    user = request.user
    if request.method == 'POST':
        user.has_medication_or_nutrition = False
        user.has_exercised = False
        user.save()
        
        # 로컬 스토리지 데이터도 초기화
        response_data = {'status': 'success'}
        return JsonResponse(response_data)
    
    return JsonResponse({'status': 'error'}, status=400)

def locker_view(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')  # 로그인 페이지로 리디렉션

    user = request.user
    
    # 연결 중인 계정과 관계 정보
    connected_users = Connection.objects.filter(Q(user1=user) | Q(user2=user))
    connected_users_with_relationship = []

    # user1-user2 mother-daughter이면 user1에게 user2는 daughter 처리
    for connected_user in connected_users:
        if connected_user.user1 == user:
            relationship = connected_user.relationship2
            other_user = connected_user.user2
        else:
            relationship = connected_user.relationship1
            other_user = connected_user.user1
            
        connected_users_with_relationship.append({
            'other_user': other_user,
            'relationship': relationship,  
    })
        
    context = {
        'user': user,
        'connected_users': connected_users_with_relationship,
    }

    return render(request,'locker.html', context)