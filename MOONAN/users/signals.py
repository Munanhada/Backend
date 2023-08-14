from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import User

# 사용자의 첫 번째 로그인 여부를 확인
@receiver(user_logged_in)
def update_first_login(sender, request, user, **kwargs):
    if user.is_authenticated and user.is_first_login:
        user.is_first_login = False
        user.save()