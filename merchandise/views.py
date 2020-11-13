from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import ProductForm

"""Code taken from Boutique Ado project and adjusted accordingly"""


def all_products(request):
    """ A view to show all products, seacch queries and sorting """

    products = Product.objects.all()

    search_query = None
    all_categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            all_categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=all_categories)
        if 'q' in request.GET:
            search_query = request.GET['q']
            if not search_query:
                messages.info(
                    request, "You didn't enter any search criteria! \
                     Here are some products")

            search_queries_products = Q(name__icontains=search_query) | Q(
                description__icontains=search_query)
            products = products.filter(search_queries_products)

            if not products:
                messages.error(
                    request, "Sorry we could not match your search!")
                return redirect(reverse('home'))

    sorting = f'{sort}_{direction}'
    context = {
        'products': products,
        'sorting': sorting,
        'search_term': search_query,
    }
    return render(request, 'merchandise/products.html', context)


def product_detail(request, product_id):
    """ A view to show detail of individual product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'merchandise/product_detail.html', context)


@login_required
def add_product(request):
    """ A view to add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access it.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        """
        Instantiate a new instance of the product form & captured
        image of the product if submitted.
        """
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                                    Please make sure, the form is valid.')
    else:
        """
        Empty form instantiation
        """
        form = ProductForm()

    template = 'merchandise/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Aview to edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access it.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        """
        Instantiated a form using request.post and request.files
        and told it the specific instance to be updated
        """
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                            Please ensure the form is valid.')
    else:
        """
        Instantiating product form using the product
        """
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'merchandise/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Aview to delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access it.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect(reverse('products'))
