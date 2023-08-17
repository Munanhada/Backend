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
        ('혈압약', '혈압약'),
        ('당뇨약', '당뇨약'),
        ('소화제', '소화제'),
        ('고지혈증약', '고지혈증약'),
        ('변비약', '변비약'),
        ('위장약', '위장약'),
        ('항생제', '항생제'),
        ('항히스타민제', '항히스타민제'),
        ('갑상선질환 치료제', '갑상선질환 치료제'),
        ('통풍 치료제', '통풍 치료제'),
        ('소염 진통제', '소염 진통제'),
        ('우울증약', '우울증약'),
        ('성호르몬제', '성호르몬제'),
    ]
    medication_name = models.CharField(max_length=100, choices=MEDICATION_CHOICES, unique=True, verbose_name='복용 중인 약')

    def __str__(self):
        return self.medication_name

class Nutrition(models.Model):
    NUTRITION_CHOICES = [
        ('유산균', '유산균'),
        ('오메가3', '오메가3'),
        ('루테인', '루테인'),
        ('종합비타민', '종합비타민'),
        ('비타민C', '비타민C'),
        ('비타민D', '비타민D'),
        ('비타민A', '비타민A'),
        ('콜라겐', '콜라겐'),
        ('철분', '철분'),
        ('프로폴리스', '프로폴리스'),
        ('아로니아', '아로니아'),
        ('엽산', '엽산'),
        ('magnesium', '마그네슘'),
        ('비타민E', '비타민E'),
        ('칼슘', '칼슘'),
    ]
    nutrition_name = models.CharField(max_length=100, choices=NUTRITION_CHOICES, unique=True, verbose_name='복용 중인 영양제')

    def __str__(self):
        return self.nutrition_name

class User(AbstractUser):
    # 사용자 기본 정보
    username = None
    name = models.CharField(max_length=20, verbose_name='이름', null=True)
    user_id = models.CharField(max_length=20, unique=True, verbose_name='아이디')
    email = models.EmailField(blank=True)
    is_first_login = models.BooleanField(default=True, verbose_name='첫 번째 로그인 여부', editable=False)

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
    med_or_nutr_status = models.BooleanField(default=False, verbose_name='복용 중인 약 및 영양제 여부', editable=True)
    medications = models.ManyToManyField(Medication, blank=True, editable=True, related_name='users_medications', through='UserMedication')
    nutritions = models.ManyToManyField(Nutrition, blank=True, editable=True, related_name='users_nutritions', through='UserNutrition')
    has_medication_or_nutrition = models.BooleanField(default=False, blank=True, verbose_name="약 및 영양제 섭취 여부")
    has_exercised = models.BooleanField(default=False, blank=True, verbose_name="운동 여부")

    def __str__(self):
        return self.name

# 연결 요청
class ConnectionRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='connection_requests_sent')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='connection_requests_received')

    RELATIONSHIP_CHOICES = [
        ('엄마', '엄마'),
        ('아빠', '아빠'),
        ('할머니', '할머니'),
        ('할아버지', '할아버지'),
        ('딸', '딸'),
        ('아들', '아들'),
        ('손자', '손자'),
        ('손녀', '손녀'),

    ]
    relationship1 = models.CharField(null=True, blank=True, max_length=100, choices=RELATIONSHIP_CHOICES, verbose_name='관계1')
    relationship2 = models.CharField(null=True, blank=True, max_length=100, choices=RELATIONSHIP_CHOICES, verbose_name='관계2')
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

# 사용자 - 약 연결하는 모델
class UserMedication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_medications')
    medication = models.ForeignKey(Medication, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='복용 중인 약')

    class Meta: 
        unique_together = ('user', 'medication') # 중복된 사용자 - 약 데이터 생성하지 않게 함

    def __str__(self):
        if self.medication:
            return str(self.medication)
        else:
            return "약이 선택되지 않았습니다."
    
# 사용자 - 영양제 연결하는 모델
class UserNutrition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_nutritions')
    nutrition = models.ForeignKey(Nutrition, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='복용 중인 영양제')

    class Meta: 
        unique_together = ('user', 'nutrition') # 중복된 사용자 - 영양제 데이터 생성하지 않게 함
    
    def __str__(self):
        if self.nutrition:
            return str(self.nutrition)
        else:
            return "영양제가 선택되지 않았습니다."
