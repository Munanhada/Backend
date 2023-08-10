from django.views.generic import TemplateView
from users.models import User, Connection, ConnectionRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
import json
from django.http import JsonResponse

def main_view(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')  # 로그인 페이지로 리디렉션

    user = request.user
    # 연결 요청 중인 경우
    connection_requests = ConnectionRequest.objects.filter(from_user=user, is_accepted=False)
    
    # 연결 요청을 받은 경우
    connection_requests_received = ConnectionRequest.objects.filter(to_user=user, is_accepted=False)

    # 연결 중인 계정과 관계 정보
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
    context = {
        'user': user,
        'connection_requests' : connection_requests,
        'connection_requests_received': connection_requests_received,
        'connected_users': connected_users_with_relationship,
    }

    return render(request, 'main.html', context)

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
        
        
    
