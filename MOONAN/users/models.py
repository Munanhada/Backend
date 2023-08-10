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
    ]
    medication_name = models.CharField(max_length=100, choices=MEDICATION_CHOICES, verbose_name='복용 중인 약')
    user_input_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='직접 입력한 약 이름')

    def __str__(self):
        return dict(self.MEDICATION_CHOICES)[self.medication_name]

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
    ]
    nutrition_name = models.CharField(max_length=100, choices=NUTRITION_CHOICES, verbose_name='복용 중인 영양제')
    user_input_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='직접 입력한 영양제 이름')

    def __str__(self):
        return dict(self.NUTRITION_CHOICES)[self.nutrition_name]

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
    birthdate = models.DateField(null=True, verbose_name='생년월일', editable=True)
    GENDER_CHOICES = [
        ('male', '남성'),
        ('female', '여성'),
    ]
    gender = models.CharField(null=True, max_length=10, choices=GENDER_CHOICES, verbose_name='성별', editable=True)
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
    relationship = models.CharField(null=True, max_length=20, choices=RELATIONSHIP_CHOICES, verbose_name='소중한 분과의 관계', editable=True)
    med_or_nutr_status = models.BooleanField(default=False, verbose_name='복용 중인 약 및 영양제 여부', editable=True)
    medications = models.ManyToManyField(Medication, blank=True, editable=True, related_name='users_medications', through='UserMedication')
    nutritions = models.ManyToManyField(Nutrition, blank=True, editable=True, related_name='users_nutritions', through='UserNutrition')

    def __str__(self):
        return self.name

# 연결 요청
class ConnectionRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='connection_requests_sent')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='connection_requests_received')
    relationship1 = models.CharField(max_length=50)
    relationship2 = models.CharField(max_length=50)
    is_accepted = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['from_user', 'to_user'], name='unique_connection_request')
        ]


# 연결 완료된
class Connection(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_users')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_users')
    relationship1 = models.CharField(max_length=50)  # 예: 'mother'
    relationship2 = models.CharField(max_length=50) # 'daughter'
    is_accepted = models.BooleanField(default=False)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user1', 'user2'], name='unique_connection')
        ]

class UserMedication(models.Model):
    # 사용자 - 약 연결하는 모델
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)

    class Meta: # 중복된 사용자 - 약 데이터 생성하지 않게 함
        unique_together = ('user', 'medication')
    
class UserNutrition(models.Model):
    # 사용자 - 영양제 연결하는 모델
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nutrition = models.ForeignKey(Nutrition, on_delete=models.CASCADE)

    class Meta: # 중복된 사용자 - 영양제 데이터 생성하지 않게 함
        unique_together = ('user', 'nutrition')
