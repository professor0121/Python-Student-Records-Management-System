from django.contrib import admin
from django.urls import path
from records import views

urlpatterns = [
    path('',views.student,name='student'),
]
