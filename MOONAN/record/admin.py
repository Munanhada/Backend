from django.contrib import admin
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['user', 'expression', 'eating', 'health', 'sleep', 'mood', 'accident', 'customContent', 'created_date']
    list_filter = ['user', 'expression', 'eating', 'health', 'sleep', 'mood', 'accident', 'created_date']

    
    