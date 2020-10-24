from django.shortcuts import render, redirect, reverse
from .models import Review
from django.contrib import messages
from .forms import ReviewForm


def all_reviews(request):
    """ A view to show all reviews """

    reviews = Review.objects.all()

    context = {
        'reviews': reviews
    }
    return render(request, 'review/all_review.html', context)


def add_review(request):

    if request.method == 'POST':
        """
        Instantiate a new instance of the review form
        """
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'Your review is added successfully!')
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'Failed to add your review. \
                                    Please make sure, the form is valid.')
    else:
        """
        Empty form instantiation
        """
        form = ReviewForm()

    template = 'review/add_review.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


