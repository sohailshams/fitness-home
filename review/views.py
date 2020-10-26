from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Review
from django.contrib import messages
from .forms import ReviewForm


def all_reviews(request):
    """ A view to show all reviews """

    reviews = Review.objects.all().order_by('-date')

    context = {
        'reviews': reviews
    }
    return render(request, 'review/all_review.html', context)


def add_review(request):
    """ A view add a review """

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


def edit_review(request, review_id):
    """ A view to edit a review """
    review = get_object_or_404(Review, pk=review_id)
    if request.user == review.user:

        review = get_object_or_404(Review, pk=review_id)
        """
        If statement to make sure onle review ownwer can access it
        """
        if request.method == 'POST':
            """
            Instantiated a form using request.post
            and told it the specific instance to be updated
            """
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your review is \
                                  updated successfully!')
                return redirect(reverse('reviews'))
            else:
                messages.error(request, 'Failed to update your review. \
                                Please ensure the form is valid.')
        else:
            """
            Instantiating review form using the review
            """
            form = ReviewForm(instance=review)
            messages.info(request, 'You are editing your review')

        template = 'review/edit_review.html'
        context = {
            'form': form,
            'review': review,
        }

        return render(request, template, context)
    else:
        messages.error(request, 'Sorry, only review owner can access it.')
        return redirect(reverse('home'))


def delete_review(request, review_id):
    """ A view to delete a review """
    review = get_object_or_404(Review, pk=review_id)
    if request.user == review.user:
        review = get_object_or_404(Review, pk=review_id)
        review.delete()
        messages.success(request, 'Review deleted successfully!')
        return redirect(reverse('reviews'))

    else:
        messages.error(request, 'Sorry, only review owner can access it.')
        return redirect(reverse('home'))
