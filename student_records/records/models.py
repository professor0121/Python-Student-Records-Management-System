# records/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class Student(models.Model):
 first_name = models.CharField(max_length=100)
 last_name = models.CharField(max_length=100)
 date_of_birth = models.DateField()
 email = models.EmailField(unique=True)
 phone_number = models.CharField(max_length=15, blank=True, null=True)
 def __str__(self):
  return f"{self.first_name} {self.last_name}"
 def get_full_name(self):
  return f"{self.first_name} {self.last_name}"
 class Meta:
  verbose_name_plural = 'Students'
class Subject(models.Model):
 name = models.CharField(max_length=100, unique=True)
 def __str__(self):
  return self.name
class Mark(models.Model):
 student = models.ForeignKey(Student, on_delete=models.CASCADE,
related_name='marks')
 subject = models.ForeignKey(Subject, on_delete=models.CASCADE,
related_name='marks')
 marks_obtained = models.DecimalField(max_digits=5, decimal_places=2,
 validators=[MinValueValidator(0),
MaxValueValidator(100)])
 def __str__(self):
  return f"{self.student.first_name} - {self.subject.name}"
 class Meta:
  unique_together = ['student', 'subject']