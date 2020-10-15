from django.urls import path
from . import views

urlpatterns = [
    path('', views.nutrition_plans, name='nutritions'),
    path('add/', views.add_nutrition, name='add_nutrition'),
]
