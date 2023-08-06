from django.contrib import admin
from users.models import User

class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_id', 'password')

admin.site.register(User, UsersAdmin)