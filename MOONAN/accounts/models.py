from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Medication(models.Model):
    MEDICATION_CHOICES = [
        ('blood_pressure', '혈압약'),
        ('diabetes', '당뇨약'),
        ('digestive', '소화제'),
        ('cholesterol', '고지혈증약'),
        ('constipation', '변비약'),
        ('digestive_system', '위장약'),
        ('antibiotics', '항생제'),
        ('antihistamines', '항히스타민제'),
        ('thyroid_disorder', '갑상선질환 치료제'),
        ('gout_treatment', '통풍 치료제'),
        ('anti-inflammatory', '소염 진통제'),
        ('antidepressants', '우울증약'),
        ('hormone_therapy', '성호르몬제'),
        ('add', '직접 입력'),
    ]
    medication_name = models.CharField(max_length=100, choices=MEDICATION_CHOICES, verbose_name='복용 중인 약', unique=True)

    def __str__(self):
        return self.medication_name

class Supplement(models.Model):
    SUPPLEMENT_CHOICES = [
        ('probiotics', '유산균'),
        ('omega3', '오메가3'),
        ('lutein', '루테인'),
        ('multivitamin', '종합비타민'),
        ('vitaminC', '비타민C'),
        ('vitaminD', '비타민D'),
        ('vitaminA', '비타민A'),
        ('collagen', '콜라겐'),
        ('iron', '철분'),
        ('propolis', '프로폴리스'),
        ('aronia', '아로니아'),
        ('folic_acid', '엽산'),
        ('magnesium', '마그네슘'),
        ('vitaminE', '비타민E'),
        ('calcium', '칼슘'),
        ('add', '직접 입력'),
    ]
    supplement_name = models.CharField(max_length=100, choices=SUPPLEMENT_CHOICES, verbose_name='복용 중인 영양제', unique=True)

    def __str__(self):
        return self.supplement_name

# 사용자의 공통 필드
class UserInfo(models.Model):
    user_info = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info', verbose_name='사용자')
    birthdate = models.DateField(verbose_name='생일')
    GENDER_CHOICES = [
        ('male', '남성'),
        ('female', '여성'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name='성별')
    RELATIONSHIP_CHOICES = [
        ('father', '아빠'),
        ('mother', '엄마'),
        ('daughter', '딸'),
        ('son', '아들'),
        ('grandmother', '할머니'),
        ('grandfather', '할아버지'),
        ('grandson', '손자'),
        ('granddaughter', '손녀'),
    ]
    relationship = models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES, verbose_name='소중한 분과의 관계')
    is_taking_meds = models.BooleanField(default=False, verbose_name='복용 중인 약 및 영양제 여부')
    medication = models.ManyToManyField(Medication, blank=True, related_name='medication')
    supplement = models.ManyToManyField(Supplement, blank=True, related_name='supplement')

    def __str__(self):
        return f"{self.user_info.user_id}의 정보"

class Child(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='children', null=True)
    user_info = models.OneToOneField(UserInfo, on_delete=models.CASCADE, related_name='child')

class Parent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parents', null=True)
    user_info = models.OneToOneField(UserInfo, on_delete=models.CASCADE, related_name='parent')