from django.shortcuts import render, redirect, reverse
from .models import ExercisePlans
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ExerciseForm

# Create your views here.


def exercise_plans(request):
    """ A view to show exercise plans """

    exercises = ExercisePlans.objects.all()

    context = {
        'exercises': exercises,
    }
    return render(request, 'exercise/exercise_plans.html', context)


@login_required
def add_exercise(request):
    """ A view to add a exercise plan to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access it.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        """
        Instantiate a new instance of the exercise form & captured
        image of the exercise plan if submitted.
        """
        form = ExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Exercise Plan added successfully!')
            return redirect(reverse('exercises',))
        else:
            messages.error(request, 'Failed to add exercise plan. \
                                    Please make sure, the form is valid.')
    else:
        """
        Empty form instantiation
        """
        form = ExerciseForm()

    template = 'exercise/add_exercise.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

