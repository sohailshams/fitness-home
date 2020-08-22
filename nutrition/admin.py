from django.contrib import admin
from .models import NutritionPlans

# Register your models here.


class NutritionPlanAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'purpose',
        'meal_plan',
        'grocery_list',
        'message',
        'coaching',
        'price',

    )

    ordering = ('price',)


admin.site.register(NutritionPlans, NutritionPlanAdmin)
