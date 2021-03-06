from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Order


@login_required
def profile(request):
    """ View to display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile updated successfully')
        else:
            messages.error(request,
                           'Update failed. Please make sure form is valid.')
    else:
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

    messages.info(request, ('Here you can see the history of your purchases.'))

    template = 'profiles/order_history.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)


def order_history_detail(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
