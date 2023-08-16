from django.contrib import admin
from .models import User, UserMedication, UserNutrition, Medication, Nutrition, Connection, ConnectionRequest

class UserMedicationInline(admin.TabularInline):
    model = UserMedication
    extra = 1  # 추가 입력 폼 수

class UserNutritionInline(admin.TabularInline):
    model = UserNutrition
    extra = 1  # 추가 입력 폼 수

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_id', 'password', 'birthdate', 'gender', 
                    'med_or_nutr_status', 'get_medications', 'get_nutritions', 
                    'has_medication_or_nutrition', 'has_exercised')
    fields = ('name', 'user_id', 'password', 'birthdate', 'gender', 
            'med_or_nutr_status','has_medication_or_nutrition', 'has_exercised')
    filter_horizontal = ('medications', 'nutritions')

    inlines = [UserMedicationInline, UserNutritionInline]

    def get_medications(self, obj):
        return ", ".join(str(medication) for medication in obj.medications.all())

    def get_nutritions(self, obj):
        return ", ".join(str(nutrition) for nutrition in obj.nutritions.all())
    
    
    
admin.site.register(User, UserAdmin) # 사용자 안에서 약/영양제 확인 가능
admin.site.register(Medication)
admin.site.register(Nutrition)
admin.site.register(UserMedication)
admin.site.register(UserNutrition)

@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ('user1', 'user2', 'relationship1', 'relationship2', 'is_accepted')
    list_filter = ('is_accepted',)
    search_fields = ('user1', 'user2', 'relationship1', 'relationship2', 'is_accepted')
    
@admin.register(ConnectionRequest)
class ConnectionRequestAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'relationship1', 'relationship2', 'is_accepted')
    list_filter = ('is_accepted',)


