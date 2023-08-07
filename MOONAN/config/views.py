from django.views.generic import TemplateView
from users.models import User, Connection
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

def connection_create_from_view(request):
    if request.method=='POST':
        from_user = request.user
        to_user = request.POST.get('to_user')
        relationship1 = request.POST.get('relationship1')
        relationship2 = request.POST.get('relationship2')
        
        try:
            to_user = get_user_model().objects.get(username=to_user)
        except get_user_model().DoesNotExist:
            # 사용자를 찾을 수 없는 경우에 대한 처리
            pass
        else:
                connection = Connection.objects.create(
                    from_user=from_user,
                    to_user=to_user,
                    relationship1=relationship1,
                    relationship2=relationship2,
                )
                # 필요한 후속 처리 (예: 연결 완료 메시지 표시)
                return redirect('connection')  # 또는 적절한 리다이렉트 경로 설정
    else:
        return render (request, 'connection.html')