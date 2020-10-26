from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

from .forms import OrderForm
from .models import Order, ProductLineItem, ExerciseLineItem, NutritionLineItem

from merchandise.models import Product
from exercise.models import ExercisePlans
from nutrition.models import NutritionPlans
from cart.contexts import cart_contents
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    Save user's data
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {
                'merchandise_dic': {},
                'excercise_plans_dic': {},
                'nutrition_plans_dic': {},
                })),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {
            'merchandise_dic': {},
            'excercise_plans_dic': {},
            'nutrition_plans_dic': {},
        })
        """
        Put the form data in a dictionay
        """
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        """
        Created an instance of the form using form data
        """
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            """
            Creation of line items
            """
            for product_type, dic in cart.items():
                if product_type == 'merchandise_dic':
                    for item_id, quantity in dic.items():
                        product = Product.objects.get(id=item_id)
                        order_line_item = ProductLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
                elif product_type == 'excercise_plans_dic':
                    for item_id, quantity in dic.items():
                        product = ExercisePlans.objects.get(id=item_id)
                        order_line_item = ExerciseLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
                elif product_type == 'nutrition_plans_dic':
                    for item_id, quantity in dic.items():
                        product = NutritionPlans.objects.get(id=item_id)
                        order_line_item = NutritionLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, ('There was an error with your form. '
                                     'Please double check your information.'))
            return redirect(reverse('checkout'))

    else:
        cart = request.session.get('cart', {
            'merchandise_dic': {},
            'excercise_plans_dic': {},
            'nutrition_plans_dic': {},
        })
        if not cart:
            messages.error(request,
                           "There is nothing in your \
                                shopping cart at the moment")
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
        """
        Prefill the checkout form with any info\
             that user maintains in his profile
        """
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'town_or_city': profile.default_town_or_city,
                    'county': profile.default_county,
                    'postcode': profile.default_postcode,
                    'country': profile.default_country,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handling of successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_full_name': order.full_name,
                'default_email': order.email,
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            """
            Created an instance of the user profile form,
            using the profile data
            """
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
