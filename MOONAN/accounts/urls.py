from django.urls import path
from .views import (join_view, id_check, login_view, send_connection_request, birth_info_view, drug_ask_view,
                    drug_info_view, add_medication, add_nutrition, logout_view)
app_name = 'accounts'

urlpatterns = [
    path('join/', join_view, name='join'),
    path('id_check/', id_check, name='id_check'),
    path('login/', login_view, name='login'),
    path('accountConnection/', send_connection_request, name='connection'),
    path('accountConnectDetailBirth/', birth_info_view, name='birth_info'),
    path('drugAsk/', drug_ask_view, name='drug_ask'),
    path('add_medication/', add_medication, name='add_medication'),
    path('add_nutrition/', add_nutrition, name='add_nutrition'),
    path('logout/', logout_view, name='logout'),
]