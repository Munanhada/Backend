from django.urls import path
from .views import record_view, submit_expression, submit_reason

app_name = 'record'

urlpatterns = [
    path('', record_view, name='home'),
    path('submit_expression/', submit_expression, name='submit_expression'),
    path('submit_reason/', submit_reason, name='submit_reason'),
]