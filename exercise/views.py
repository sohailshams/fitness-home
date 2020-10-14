from django.shortcuts import render, redirect, reverse, get_object_or_404
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
            return redirect(reverse('exercises'))
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


@login_required
def edit_exercise(request, exercise_id):
    """ Aview to edit an exercise plan in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access it.')
        return redirect(reverse('home'))

    exercise = get_object_or_404(ExercisePlans, pk=exercise_id)
    if request.method == 'POST':
        """
        Instantiated a form using request.post and request.files
        and told it the specific instance to be updated
        """
        form = ExerciseForm(request.POST, request.FILES, instance=exercise)
        if form.is_valid():
            form.save()
            messages.success(request, f'Exercise Plan {exercise.name} \
                                        updated successfully!')
            return redirect(reverse('exercises'))
        else:
            messages.error(request, 'Failed to update exercise plan. \
                            Please ensure the form is valid.')
    else:
        """
        Instantiating exercise plan form using the exercise plan
        """
        form = ExerciseForm(instance=exercise)
        messages.info(request, f'You are editing exercise \
                                plan {exercise.name}')

    template = 'exercise/edit_exercise.html'
    context = {
        'form': form,
        'exercise': exercise,
    }

    return render(request, template, context)
