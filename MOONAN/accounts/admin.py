from django.contrib import admin
from .models import Child, Parent
from users.models import User, Medication, Nutrition

class ChildAdmin(admin.ModelAdmin):
    list_display = ('birthdate', 'gender', 'relationship', 'is_taking_meds', 'get_medications', 'get_nutritions')

    def birthdate(self, obj):
        return obj.user.birthdate

    def gender(self, obj):
        return obj.user.gender

    def relationship(self, obj):
        return obj.user.relationship
    
    def is_taking_meds(self, obj):
        return obj.user.is_taking_meds
    
    def get_medications(self, obj):
        medications = obj.medications.all()
        return ", ".join(str(medication) for medication in medications)

    def get_nutritions(self, obj):
        nutritions = obj.nutritions.all()
        return ", ".join(str(nutrition) for nutrition in nutritions)


admin.site.register(Child, ChildAdmin)

class ParentAdmin(admin.ModelAdmin):
    list_display = ('birthdate', 'gender', 'relationship', 'is_taking_meds', 'get_medications', 'get_nutritions')

    def birthdate(self, obj):
        return obj.user.birthdate

    def gender(self, obj):
        return obj.user.gender

    def relationship(self, obj):
        return obj.user.relationship
    
    def is_taking_meds(self, obj):
        return obj.user.is_taking_meds

    def get_medications(self, obj):
        medications = obj.medications.all()
        return ", ".join(str(medication) for medication in medications)

    def get_nutritions(self, obj):
        nutritions = obj.nutritions.all()
        return ", ".join(str(nutrition) for nutrition in nutritions)
    
admin.site.register(Parent, ParentAdmin)