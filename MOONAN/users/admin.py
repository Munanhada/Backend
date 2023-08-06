from django.contrib import admin
from .models import User, Medication, Nutrition, UserMedication, UserNutrition

class UserMedicationInline(admin.TabularInline):
    model = UserMedication

class UserNutritionInline(admin.TabularInline):
    model = UserNutrition

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_id', 'password', 
                    'birthdate', 'gender', 'relationship', 'is_taking_meds', 'get_medications', 'get_nutritions')
    fields = ('name', 'user_id', 'password',
            'birthdate', 'gender', 'relationship', 'is_taking_meds')

    inlines = [UserMedicationInline, UserNutritionInline]

    def get_medications(self, obj):
        user_medications = obj.medications.all()
        return ", ".join(str(medication.medication) for medication in user_medications)

    def get_nutritions(self, obj):
        user_nutritions = obj.nutritions.all()
        return ", ".join(str(nutrition.nutrition) for nutrition in user_nutritions)


admin.site.register(User, UserAdmin)
admin.site.register(Medication)
admin.site.register(Nutrition)