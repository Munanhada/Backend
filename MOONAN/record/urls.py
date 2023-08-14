from django.urls import path
from .views import record_view, expression_button_highlight

app_name = 'record'

urlpatterns = [
    path('', record_view, name='record'),
    path('/expression_button_highlight', expression_button_highlight, name='highlight')
]