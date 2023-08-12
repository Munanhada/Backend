"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from config.views import home_view, accept_connection_request, reject_connection_request, alarm_view
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='home', permanent=False)),
    path('home/', home_view, name='home'),
    path('home/alarm/', alarm_view, name='alarm'),
    path('accept_connection_request/', accept_connection_request, name='accept_connection_request'),
    path('reject_connection_request/', reject_connection_request, name='reject_connection_request'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
