from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from merchandise.models import Product
from exercise.models import ExercisePlans
from nutrition.models import NutritionPlans

# Create your views here.


def view_cart(request):
    """ A view that renders the shopping cart page"""
    return render(request, 'cart/shopping_cart.html')

# Chris Zielinski helped to write the code for following add_cart function


def add_cart(request, item_id):
    """ Add quantity of specified product to the shopping cart """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    product_type = request.POST.get('product_type')
    cart = request.session.get('cart', {
        'merchandise_dic': {},
        'excercise_plans_dic': {},
        'nutrition_plans_dic': {},
    })

    if product_type == 'merchandise':
        product = get_object_or_404(Product, pk=item_id)
        if item_id in cart['merchandise_dic'].keys():
            cart['merchandise_dic'][item_id] += quantity
            messages.success(request, f'{product.name} added to cart')
        else:
            cart['merchandise_dic'][item_id] = quantity
            messages.success(request, f'{product.name} added to cart')
    elif product_type == 'excercise_plan':
        exercise = get_object_or_404(ExercisePlans, pk=item_id)
        if cart['excercise_plans_dic']:
            messages.success(
                request,
                'Exercise Plan is already added in the shopping cart please \
                    proceed to the payment or update new Exercise Plan by \
                        deleting one from shopping cart.')
        else:
            cart['excercise_plans_dic'][item_id] = quantity
            messages.success(
                request,
                f'{exercise.name} exercise plan added to cart')
    else:
        nutrition = get_object_or_404(NutritionPlans, pk=item_id)
        if item_id in cart['nutrition_plans_dic'].keys():
            cart['nutrition_plans_dic'][item_id] += quantity
            messages.success(
                request,
                f'{nutrition.name} nutrition plan added to cart')
        else:
            cart['nutrition_plans_dic'][item_id] = quantity
            messages.success(
                request,
                f'{nutrition.name} nutrition plan added to cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Update the quantity of specified product in the shopping cart """
    quantity = int(request.POST.get('quantity'))
    product = get_object_or_404(Product, pk=item_id)
    cart = request.session.get('cart', {
        'merchandise_dic': {},
        'excercise_plans_dic': {},
        'nutrition_plans_dic': {},
    })
    if item_id in cart['merchandise_dic'].keys():
        if quantity > 0:
            cart['merchandise_dic'][item_id] = quantity
            messages.success(request, f'Updated {product.name} \
                Quantity: {cart["merchandise_dic"][item_id]}')
        else:
            cart['merchandise_dic'].pop(item_id)
            messages.success(request, f'Removed {product.name} from cart')
    else:
        cart['merchandise_dic'].pop(item_id)
        messages.success(request, f'Removed {product.name} from cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, category, item_id):
    """ Delete the specified item from the shopping cart """
    cart = request.session.get('cart', {
        'merchandise_dic': {},
        'excercise_plans_dic': {},
        'nutrition_plans_dic': {},
    })
    try:
        if category == 'merchandise_dic':
            product = get_object_or_404(Product, pk=item_id)
            if item_id in cart['merchandise_dic'].keys():
                cart['merchandise_dic'].pop(item_id)
                messages.success(request, f'Removed {product.name} from cart')
        elif category == 'excercise_plans_dic':
            exercise = get_object_or_404(ExercisePlans, pk=item_id)
            if item_id in cart['excercise_plans_dic'].keys():
                cart['excercise_plans_dic'].pop(item_id)
                messages.success(
                    request,
                    f'Removed {exercise.name} exercise plan from cart')
        elif category == 'nutrition_plans_dic':
            nutrition = get_object_or_404(NutritionPlans, pk=item_id)
            if item_id in cart['nutrition_plans_dic'].keys():
                cart['nutrition_plans_dic'].pop(item_id)
                messages.success(
                    request,
                    f'Removed {nutrition.name} nutrition plan from cart')

        request.session['cart'] = cart
        return redirect(reverse('view_cart'))
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return redirect(reverse('view_cart'))
