from django.views.generic import TemplateView
from users.models import User
from django.shortcuts import get_object_or_404, render, redirect

class ConnectView(TemplateView):
    temolate_name = 'connection.html'