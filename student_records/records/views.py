# records/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student, Mark, Subject
from .forms import StudentForm, MarkForm
from django.contrib import messages
class StudentListView(ListView):
 model = Student
 template_name = 'records/student_list.html'
 context_object_name = 'students'
 
 
class StudentDetailView(DetailView):
 model = Student
 template_name = 'records/student_detail.html'
 context_object_name = 'student'
 
 
class StudentCreateView(CreateView):
 model = Student
 form_class = StudentForm
 template_name = 'records/student_form.html'
 success_url = reverse_lazy('student_list')
 def form_valid(self, form):
  messages.success(self.request, "Student created successfully!")
  return super().form_valid(form)


class StudentUpdateView(UpdateView):
 model = Student
 form_class = StudentForm
 template_name = 'records/student_form.html'
 success_url = reverse_lazy('student_list')
 def form_valid(self, form):
  messages.success(self.request, "Student updated successfully!")
  return super().form_valid(form)


class StudentDeleteView(DeleteView):
 model = Student
 template_name = 'records/student_confirm_delete.html'
 success_url = reverse_lazy('student_list')
 def delete(self, request, *args, **kwargs):
  messages.success(self.request, "Student deleted successfully!")
  return super().delete(request, *args, **kwargs)


class MarkCreateView(CreateView):
 model = Mark
 form_class = MarkForm
 template_name = 'records/mark_form.html'
 success_url = reverse_lazy('student_list')
 def form_valid(self, form):
  messages.success(self.request, "Mark added successfully!")
  return super().form_valid(form)


class MarkDeleteView(DeleteView):
 model = Mark
 template_name = 'records/mark_confirm_delete.html'
 def get_success_url(self):
  return reverse_lazy('student_detail', kwargs={'pk':
self.object.student.id})
 def delete(self, request, *args, **kwargs):
  messages.success(self.request, "Mark deleted successfully!")
  return super().delete(request, *args, **kwargs)


class MarkDetailView(DetailView):
    model = Mark
    template_name = 'records/mark_detail.html'
    context_object_name = 'mark'
    
    
class MarkDeleteView(DeleteView):
    model = Mark
    template_name = 'records/mark_confirm_delete.html'
    success_url = reverse_lazy('student_list')
    def get_success_url(self):
        return reverse_lazy('student_detail', kwargs={'pk': self.object.student.id})

