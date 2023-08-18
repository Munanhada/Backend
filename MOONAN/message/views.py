from django.shortcuts import render
from message.models import Message
from django.http import JsonResponse
from users.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

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
    