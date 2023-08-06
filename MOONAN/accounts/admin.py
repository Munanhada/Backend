from django.contrib import admin
from .models import UserInfo, Child, Parent, Medication, Supplement

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user_info', 'birthdate', 'gender', 'relationship', 'is_taking_meds', 'get_medication', 'get_supplement')

    def get_medication(self, obj):
        return ', '.join([str(med) for med in obj.medication.all()])
    
    def get_supplement(self, obj):
        return ', '.join([str(s) for s in obj.supplement.all()])

admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Medication)
admin.site.register(Supplement)
    
class ChildAdmin(admin.ModelAdmin):
    list_display = ('user_info', 'birthdate', 'gender', 'relationship', 'is_taking_meds', 'get_medication', 'get_supplement')

    def birthdate(self, obj):
        return obj.user_info.birthdate

    def gender(self, obj):
        return obj.user_info.gender

    def relationship(self, obj):
        return obj.user_info.relationship
    
    def is_taking_meds(self, obj):
        return obj.user_info.is_taking_meds
    
    def get_medication(self, obj):
        return ', '.join([str(med) for med in obj.medication.all()])
    
    def get_supplement(self, obj):
        return ', '.join([str(s) for s in obj.supplement.all()])


admin.site.register(Child, ChildAdmin)

class ParentAdmin(admin.ModelAdmin):
    list_display = ('user_info', 'birthdate', 'gender', 'relationship', 'is_taking_meds', 'get_medication', 'get_supplement')

    def birthdate(self, obj):
        return obj.user_info.birthdate

    def gender(self, obj):
        return obj.user_info.gender

    def relationship(self, obj):
        return obj.user_info.relationship
    
    def is_taking_meds(self, obj):
        return obj.user_info.is_taking_meds

    def get_medication(self, obj):
        return ', '.join([str(med) for med in obj.medication.all()])
    
    def get_supplement(self, obj):
        return ', '.join([str(s) for s in obj.supplement.all()])
    
admin.site.register(Parent, ParentAdmin)