from django.contrib import admin
from .models import User, Medication, Nutrition, Connection, ConnectionRequest

class UserMedicationInline(admin.TabularInline):
    model = User.medications.through

class UserNutritionInline(admin.TabularInline):
    model = User.nutritions.through

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_id', 'password', 
                    'birthdate', 'gender', 'relationship', 'med_or_nutr_status', 'get_medications', 'get_nutritions')
    fields = ('name', 'user_id', 'password',
            'birthdate', 'gender', 'relationship', 'med_or_nutr_status')
    filter_horizontal = ('medications', 'nutritions')

    inlines = [UserMedicationInline, UserNutritionInline]

    def get_medications(self, obj):
        return ", ".join(str(medication) for medication in obj.medications.all())

    def get_nutritions(self, obj):
        return ", ".join(str(nutrition) for nutrition in obj.nutritions.all())

class MedicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'medication_name', 'get_users_taking_medication')

    def get_users_taking_medication(self, obj):
        user_medications = obj.usermedication_set.all()
        return ", ".join(str(user_medication.user) for user_medication in user_medications)

    get_users_taking_medication.short_description = '약을 복용하는 사용자'

class NutritionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nutrition_name', 'get_users_taking_nutrition')

    def get_users_taking_nutrition(self, obj):
        user_nutritions = obj.usernutrition_set.all()
        return ", ".join(str(user_nutrition.user) for user_nutrition in user_nutritions)

    get_users_taking_nutrition.short_description = '영양제를 복용하는 사용자'

@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'relationship1', 'relationship2', 'is_accepted')
    list_filter = ('is_accepted',)
    search_fields = ('from_user', 'to_user', 'relationship1', 'relationship2', 'is_accepted')
    
@admin.register(ConnectionRequest)
class ConnectionRequestAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'relationship1', 'relationship2', 'is_accepted')
    list_filter = ('is_accepted',)
    
admin.site.register(User, UserAdmin)
admin.site.register(Medication, MedicationAdmin)
admin.site.register(Nutrition, NutritionAdmin)
