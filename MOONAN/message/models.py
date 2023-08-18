from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='received_messages')
    RECOMMENDCONTENT_CHOICES = [
        ('벚꽃이 안개한 요즘, 벚꽃 보면 어떤 생각 들어?', '벚꽃이 안개한 요즘, 벚꽃 보면 어떤 생각 들어?'),
        ('요새 가장 땡기는 음식은?', '요새 가장 땡기는 음식은?'),
        ('놀러가고 싶은 곳은 없어?', '놀러가고 싶은 곳은 없어?'),
        ('더운 날씨, 무더위 조심해, 별 일 없지?', '더운 날씨, 무더위 조심해, 별 일 없지?'),
        ('보고 싶어', '보고 싶어'),
        
    ]
    recommendContent = models.CharField(null=True, blank=True, max_length=100, choices=RECOMMENDCONTENT_CHOICES, verbose_name='추천하는 메시지', editable=True)
    customContent = models.TextField(null=True, blank=True)  # 사용자가 직접 입력할 내용
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.recommendContent:
            return f"From: {self.sender} To: {self.receiver} - {self.get_recommendContent_display()}"
        else:
            return f"From: {self.sender} To: {self.receiver} - {self.customContent}"
    
    def clean(self):
        if self.recommendContent and self.customContent:
            raise ValidationError("추천 메시지와 직접 작성 메시지 중 하나만 선택하세요.")