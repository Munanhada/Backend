from django.urls import path
from .views import join_view, id_check, login_view, send_connection_request, info_view, logout_view

app_name = 'accounts'

urlpatterns = [
    path('join/', join_view, name='join'),
    path('id_check/', id_check, name='id_check'),
    path('login/', login_view, name='login'),
    path('accountConnection/', send_connection_request, name='connection'),
    path('info/', info_view, name='info'),
    path('logout/', logout_view, name='logout'),
]