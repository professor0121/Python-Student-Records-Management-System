# records/forms.py
from django import forms
from .models import Student, Mark, Subject
# Form for creating or editing student records
class StudentForm(forms.ModelForm):
 class Meta:
  model = Student
  fields = ['first_name', 'last_name', 'date_of_birth', 'email','phone_number']
# Form for creating or editing mark records
class MarkForm(forms.ModelForm):
 class Meta:
  model = Mark
  fields = ['student', 'subject', 'marks_obtained']
  def clean_marks_obtained(self):
   marks = self.cleaned_data.get('marks_obtained')
   if marks < 0 or marks > 100:
    raise forms.ValidationError("Marks must be between 0 and 100")
   return marks