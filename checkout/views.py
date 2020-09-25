from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {
        'merchandise_dic': {},
        'excercise_plans_dic': {},
        'nutrition_plans_dic': {},
    })
    if not cart:
        messages.error(request,
                       "There's nothing in your shopping cart at the moment")
        return redirect(reverse('products'))

    """ Got total from cart_contents """
    current_cart = cart_contents(request)
    current_total = current_cart['total']
    stripe_total = round(current_total * 100)
    """ Set secret key on stripe """
    stripe.api_key = stripe_secret_key
    """ Created payment intent """
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
        )

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)

