from django.views.generic import TemplateView
from users.models import User, Connection
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

def main_view(request):
    user = request.user
    connected_users = Connection.objects.filter(from_user=user)
    
    connected_users_with_relationship = []

    # user1-user2 mother-daughter이면 user1에게 user2는 daughter 처리
    for connected_user in connected_users:
        if connected_user.from_user == user:
            relationship = connected_user.relationship2
            other_user_name = connected_user.to_user.name
        else:
            relationship = connected_user.relationship1
            other_user_name = connected_user.from_user.name
        
        connected_users_with_relationship.append({
            'other_user_name': other_user_name,
            'relationship': relationship,  
        })
    context = {
        'user': user,
        'connected_users': connected_users_with_relationship,
    }

    return render(request, 'main.html', context)
