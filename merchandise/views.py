from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show all products, seacch queries and sorting """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'merchandise/products.html', context)


def product_detail(request, product_id):
    """ A view to show detail of individual product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'merchandise/product_detail.html', context)
