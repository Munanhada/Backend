from django.urls import path
from .views import (join_view, id_check, login_view, send_connection_request, birth_info_view, drug_ask_view,
                    drug_info_view, med_nutr_data, add_medication, add_nutrition, add_connection_request, logout_view)
app_name = 'accounts'

urlpatterns = [
    path('join/', join_view, name='join'),
    path('id_check/', id_check, name='id_check'),
    path('login/', login_view, name='login'),
    path('accountConnection/', send_connection_request, name='connection'),
    path('addAccountConnection/', add_connection_request, name='add_connection'),
    path('accountBirth/', birth_info_view, name='birth_info'),
    path('drugAsk/', drug_ask_view, name='drug_ask'),
    path('drugYes/', drug_info_view, name='drug_info'),
    path('med_nutr_data/', med_nutr_data, name='med_nutr_data'),
    path('add_medication/', add_medication, name='add_medication'),
    path('add_nutrition/', add_nutrition, name='add_nutrition'),
    path('logout/', logout_view, name='logout'),
]