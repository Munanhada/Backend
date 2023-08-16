from django.urls import path
from .views import record_view, submit_data

app_name = 'record'

urlpatterns = [
    path('', record_view, name='home'),
    path('submit_data/', submit_data, name='submit_data'),
]