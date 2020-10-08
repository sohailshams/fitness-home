from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages

from checkout.models import Order


def profile(request):
    """ View to display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    """
    Populate the form with currents user's information
    """
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all().order_by('-date')

    template = 'profiles/order_history.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)

