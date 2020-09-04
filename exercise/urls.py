from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercise_plans, name='exercises'),
]
