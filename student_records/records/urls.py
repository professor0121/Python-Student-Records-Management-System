# records/urls.py
from django.urls import path
from . import views
urlpatterns = [
 path('', views.StudentListView.as_view(), name='student_list'),
 path('student/<int:pk>/', views.StudentDetailView.as_view(),name='student_detail'),
 path('student/create/', views.StudentCreateView.as_view(), name='student_create'),
 path('student/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
 path('student/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
 path('marks/create/', views.MarkCreateView.as_view(), name='mark_create'),
 path('marks/<int:pk>/', views.MarkDetailView.as_view(), name='mark_detail'),
 path('marks/<int:pk>/delete/', views.MarkDeleteView.as_view(), name='mark_delete'),
 path('marks/<int:pk>/delete/', views.MarkDeleteView.as_view(), name='mark_delete'),

]
