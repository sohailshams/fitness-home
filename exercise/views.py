from django.shortcuts import render
from .models import ExercisePlans

# Create your views here.


def exerxise_plans(request):
    """ A view to show exerxise plans """

    exercises = ExercisePlans.objects.all()

    context = {
        'exercises': exercises
    }
    return render(request, 'exercise/exercise_plans.html', context)
