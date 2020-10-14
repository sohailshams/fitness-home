from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercise_plans, name='exercises'),
    path('add/', views.add_exercise, name='add_exercise'),
]
