from django.contrib import admin
from .models import User, Medication, Nutrition

class UserMedicationInline(admin.TabularInline):
    model = User.medications.through

class UserNutritionInline(admin.TabularInline):
    model = User.nutritions.through

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_id', 'password', 
                    'birthdate', 'gender', 'relationship', 'is_taking_meds', 'get_medications', 'get_nutritions')
    fields = ('name', 'user_id', 'password',
            'birthdate', 'gender', 'relationship', 'is_taking_meds')

    inlines = [UserMedicationInline, UserNutritionInline]

    def get_medications(self, obj):
        medications = obj.medications.all()
        return ", ".join(str(medication) for medication in medications)

    def get_nutritions(self, obj):
        nutritions = obj.nutritions.all()
        return ", ".join(str(nutrition) for nutrition in nutritions)


admin.site.register(User, UserAdmin)
admin.site.register(Medication)
admin.site.register(Nutrition)