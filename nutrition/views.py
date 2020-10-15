from django.shortcuts import render, redirect, reverse
from .models import NutritionPlans
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import NutritionForm

# Create your views here.


def nutrition_plans(request):
    """ A view to show nutrition plans """

    nutritions = NutritionPlans.objects.all()

    context = {
        'nutritions': nutritions
    }
    return render(request, 'nutrition/nutrition_plans.html', context)


@login_required
def add_nutrition(request):
    """ A view to add a nutrition plan to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access it.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        """
        Instantiate a new instance of the nutrition form & captured
        image of the nutrition plan if submitted.
        """
        form = NutritionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nutrition Plan added successfully!')
            return redirect(reverse('nutritions'))
        else:
            messages.error(request, 'Failed to add nutrition plan. \
                                    Please make sure, the form is valid.')
    else:
        """
        Empty form instantiation
        """
        form = NutritionForm()

    template = 'nutrition/add_nutrition.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

