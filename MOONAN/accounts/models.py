from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Child(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='children', null=True)

<<<<<<< Updated upstream
class Parent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parents', null=True)
    user_info = models.OneToOneField(UserInfo, on_delete=models.CASCADE, related_name='parent')
=======
    def __str__(self):
        return self.user.full_name

class Parent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parents', null=True)

    def __str__(self):
        return self.user.full_name
>>>>>>> Stashed changes
