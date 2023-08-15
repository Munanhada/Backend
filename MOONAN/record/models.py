from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils import timezone

class Record(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    EXPRESSION_CHOICES = [
        ('best', '최고예요'),
        ('munan', '무난해요'),
        ('soso', '그럭저럭'),
        ('notgood', '안좋아요'),
        ('bad', '나빠요'),
    ]
    EATING_CHOICES = [
        ('입맛이 없었어.. 시원한게 먹고 싶구나', 1),
        ('소화가 잘 안되네..', 2),
        ('맛이 없었어..', 3),
        ('이가 아파서 먹기 힘들었어..', 4),
        ('더부룩하고 체기가 있었어..', 5),
        ('먹고싶은 음식이 아니었어..', 6),
    ]
    HEALTH_CHOICES = [
        ('무릎이 아프네..', 1),
        ('비가 오려나 몸이 쑤시네..', 2),
        ('머리가 아프네..', 3),
        ('허리가 아프네..', 4),
        ('가슴이 답답하네..', 5),
        ('감기기운이 있나봐..', 6),
    ]
    SLEEP_CHOICES = [
        ('밤새악몽을 꿨어', 1),
        ('잠이 안와서 뒤척였어..', 2),
        ('자꾸 깼어ㅠㅠ', 3),
        ('화장실을 자주 갔어..', 4),
        ('자는데 소음때문에 힘들었어', 5),
    ]
    MOOD_CHOICES = [
        ('오늘은 좀 울적하네..', 1),
        ('오늘은 좀 꿀꿀해', 2),
        ('오늘 좀 심심했어', 3),
        ('오늘 답답한 일이 있었어..', 4),
        ('화가나는 일이 있었어!', 5),
        ('짜증나는 일이 있었어!', 6),
    ]
    ACCIDENTS_CHOICES = [
        ('부딪혀서 멍이 들었어', 1),
        ('요리하다 살짝 데였어', 2),
        ('요리하다 살짝 베었어', 3),
        ('발에 걸려서 넘어졌어', 4),
        ('교통사고 났어', 5),
    ]
    expression = models.CharField(null=True, max_length=20, choices=EXPRESSION_CHOICES, verbose_name='표정')
    eating = models.CharField(null=True, blank=True, max_length=100, choices=EATING_CHOICES, verbose_name='식사')
    health = models.CharField(null=True, blank=True,  max_length=100, choices=HEALTH_CHOICES, verbose_name='건강')
    sleep = models.CharField(null=True, blank=True, max_length=100, choices=SLEEP_CHOICES, verbose_name='수면')
    mood = models.CharField(null=True, blank=True, max_length=100, choices=MOOD_CHOICES, verbose_name='기분')
    accident = models.CharField(null=True, blank=True, max_length=100, choices=ACCIDENTS_CHOICES, verbose_name='사고')
    customContent = models.TextField(null=True, blank=True)  # 사용자가 직접 입력할 내용
    happyorsad = models.TextField(null=True, blank=True)  # 기쁘거나 슬펐던 일

    created_date = models.DateField(default=timezone.now)
