# records/admin.py
from django.contrib import admin
from .models import Student, Mark, Subject
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
 list_display = ['first_name', 'last_name', 'email', 'date_of_birth']
 search_fields = ['first_name', 'last_name', 'email']
@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
 list_display = ['student', 'subject', 'marks_obtained']
 search_fields = ['student__first_name', 'student__last_name',
'subject__name']
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
 list_display = ['name']
