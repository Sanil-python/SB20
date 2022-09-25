from django.contrib import admin
from .models import ExamCenter,ProxyExamCenter

# Register your models here.

@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname','city']

@admin.register(ProxyExamCenter)
class ProxyExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']