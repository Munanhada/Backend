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
        return ", ".join([medication.medication_name for medication in obj.medications.all()])

    def get_nutritions(self, obj):
        return ", ".join([nutrition.nutrition_name for nutrition in obj.nutritions.all()])


admin.site.register(User, UserAdmin)
admin.site.register(Medication)
admin.site.register(Nutrition)