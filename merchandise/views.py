from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product


# Create your views here.
def all_products(request):
    """ A view to show all products, seacch queries and sorting """

    products = Product.objects.all()

    search_query = None

    if request.GET:
        if 'q' in request.GET:
            search_query = request.GET['q']

            search_queries_products = Q(name__icontains=search_query) | Q(description__icontains=search_query)
            products = products.filter(search_queries_products)

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
