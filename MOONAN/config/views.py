from django.views.generic import TemplateView
from users.models import User
from django.shortcuts import get_object_or_404, render, redirect

class ConnectView(TemplateView):
    template_name = 'connection.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 추가적인 컨텍스트 데이터를 설정하고 싶다면 여기서 설정하세요.
        return context