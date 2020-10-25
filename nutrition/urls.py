from django.urls import path
from . import views

urlpatterns = [
    path('', views.nutrition_plans, name='nutritions'),
    path('add/', views.add_nutrition, name='add_nutrition'),
    path('edit/<int:nutrition_id>/', views.edit_nutrition,
         name='edit_nutrition'),
    path('delete/<int:nutrition_id>/', views.delete_nutrition,
         name='delete_nutrition'),
]
