# records/admin.py
from django.contrib import admin
from .models import Student, Mark, Subject


admin.site.site_header = "🎓 Student Management Admin"
admin.site.site_title = "Student Admin"
admin.site.index_title = "Welcome to the Student Management Portal"


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
