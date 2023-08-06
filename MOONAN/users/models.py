from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from django.db import models

class UserManager(DjangoUserManager):
    def _create_user(self, name, user_id, password=None, **extra_fields):
        # 아이디 필수 입력
        if not user_id:
            raise ValueError('아이디는 필수 값입니다.')
        
        # 아이디 중복 체크
        if self.model.objects.filter(user_id=user_id).exists():
            raise ValueError('이미 사용 중인 아이디입니다.')
        
        user = self.model(name=name, user_id=user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name, user_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name,user_id, password, **extra_fields)

    def create_superuser(self, name, user_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(name, user_id, password, **extra_fields)
    
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
    medication_name = models.CharField(max_length=100, choices=MEDICATION_CHOICES, verbose_name='복용 중인 약')

    def __str__(self):
        return self.medication_name

class Nutrition(models.Model):
    NUTRITION_CHOICES = [
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
    nutrition_name = models.CharField(max_length=100, choices=NUTRITION_CHOICES, verbose_name='복용 중인 영양제')

    def __str__(self):
        return self.nutrition_name
    
class User(AbstractUser):
    # 사용자 기본 정보
    username = None
    name = models.CharField(max_length=20, verbose_name='이름', null=True)
    user_id = models.CharField(max_length=20, unique=True, verbose_name='아이디')
    email = models.EmailField(blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'user_id' # username 대신 user_id을 사용
    REQUIRED_FIELDS = ['name']

    # 사용자 추가 정보
    birthdate = models.DateField(null=True, verbose_name='생일')
    GENDER_CHOICES = [
        ('male', '남성'),
        ('female', '여성'),
    ]
    gender = models.CharField(null=True, max_length=10, choices=GENDER_CHOICES, verbose_name='성별')
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
    relationship = models.CharField(null=True, max_length=20, choices=RELATIONSHIP_CHOICES, verbose_name='소중한 분과의 관계')
    is_taking_meds = models.BooleanField(default=False, verbose_name='복용 중인 약 및 영양제 여부')
    medications = models.ManyToManyField(Medication, blank=True, related_name='users_medications')
    nutritions = models.ManyToManyField(Nutrition, blank=True, related_name='users_nutritions')

    def __str__(self):
        return self.name