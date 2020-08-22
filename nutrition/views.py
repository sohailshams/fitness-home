from django.shortcuts import render
from .models import NutritionPlans

# Create your views here.


def nutrition_plans(request):
    """ A view to show nutrition plans """

    nutritions = NutritionPlans.objects.all()

    context = {
        'nutritions': nutritions
    }
    return render(request, 'nutrition/nutrition_plans.html', context)
