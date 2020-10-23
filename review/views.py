from django.shortcuts import render
from .models import Review


def all_reviews(request):
    """ A view to show all reviews """

    reviews = Review.objects.all()

    context = {
        'reviews': reviews
    }
    return render(request, 'review/all_review.html', context)
