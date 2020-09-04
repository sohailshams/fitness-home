from django.shortcuts import render
from .models import ExercisePlans

# Create your views here.


def exercise_plans(request):
    """ A view to show exercise plans """

    exercises = ExercisePlans.objects.all()

    context = {
        'exercises': exercises
    }
    return render(request, 'exercise/exercise_plans.html', context)
