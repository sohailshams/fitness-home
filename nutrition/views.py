from django.shortcuts import render, redirect, reverse, get_object_or_404
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


@login_required
def edit_nutrition(request, nutrition_id):
    """ Aview to edit a nutrition plan in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access it.')
        return redirect(reverse('home'))

    nutrition = get_object_or_404(NutritionPlans, pk=nutrition_id)
    if request.method == 'POST':
        """
        Instantiated a form using request.post and request.files
        and told it the specific instance to be updated
        """
        form = NutritionForm(request.POST, request.FILES, instance=nutrition)
        if form.is_valid():
            form.save()
            messages.success(request, f'Nutrition Plan {nutrition.name} \
                                        updated successfully!')
            return redirect(reverse('nutritions'))
        else:
            messages.error(request, 'Failed to update nutrition plan. \
                            Please ensure the form is valid.')
    else:
        """
        Instantiating nutrition plan form using the nutrition plan
        """
        form = NutritionForm(instance=nutrition)
        messages.info(request, f'You are editing nutrition \
                                plan {nutrition.name}')

    template = 'nutrition/edit_nutrition.html'
    context = {
        'form': form,
        'nutrition': nutrition,
    }

    return render(request, template, context)


@login_required
def delete_nutrition(request, nutrition_id):
    """ A view to delete a nutrition plan from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access it.')
        return redirect(reverse('home'))

    nutrition = get_object_or_404(NutritionPlans, pk=nutrition_id)
    nutrition.delete()
    messages.success(request, f'Nutrition Plan {nutrition.name} \
                                deleted successfully!')
    return redirect(reverse('nutritions'))