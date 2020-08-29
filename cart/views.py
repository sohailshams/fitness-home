from django.shortcuts import render, redirect

# Create your views here.


def view_cart(request):
    """ A view that renders the shopping cart page"""
    return render(request, 'cart/shopping_cart.html')


def add_cart(request, item_id):
    """ Add quantity of specified product to the shopping cart """
    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
        
    request.session['cart'] = cart
    return redirect(redirect_url)
