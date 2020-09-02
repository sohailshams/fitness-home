from django.shortcuts import render, redirect

# Create your views here.


def view_cart(request):
    """ A view that renders the shopping cart page"""
    return render(request, 'cart/shopping_cart.html')


def add_cart(request, item_id):
    """ Add quantity of specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    product_type = request.POST.get('product_type')
    cart = request.session.get('cart', {
        'merchandise': {},
        'excercise_plans': {},
        'nutrition_plans': {},
    })

    item_in_cart = any([
        item_id in cart['merchandise'].keys(),
        item_id in cart['excercise_plans'].keys(),
        item_id in cart['nutrition_plans'].keys(),
    ])

    if item_in_cart:
        if product_type == 'merchandise':
            cart['merchandise'][item_id] += quantity
        elif product_type == 'excercise_plan':
            cart['excercise_plans'][item_id] += quantity
        else:
            cart['nutrition_plans'][item_id] += quantity
    else:
        if product_type == 'merchandise':
            cart['merchandise'][item_id] = quantity
        elif product_type == 'excercise_plan':
            cart['excercise_plans'][item_id] = quantity
        else:
            cart['nutrition_plans'][item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
