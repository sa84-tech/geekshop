from django.shortcuts import render, get_object_or_404

from cartapp.models import Cart
from geekshop.views import get_count, get_total
from .models import Product, ProductCategory


def product_list(request, pk=None):
    title = 'каталог'
    menu_items = ProductCategory.objects.all()
    product_count = get_count(request.user)
    total_cost = get_total(request.user)

    if pk:
        products = Product.objects.filter(category_id=pk)[:9]
    else:
        products = Product.objects.all()[:9]

    context = {
        'title': title,
        'menu_items': menu_items,
        'products': products,
        'count': product_count,
        'total_cost': total_cost,
    }

    return render(request, 'mainapp/product_list.html', context)


def product_details(request, pk=None):
    print(pk)
    title = 'каталог'
    menu_items = ProductCategory.objects.all()

    product_count = get_count(request.user)
    total_cost = get_total(request.user)

    if pk:
        product = get_object_or_404(Product, pk=pk)
        products = Product.objects.filter(category_id=product.category).exclude(pk=pk)[:3]
    else:
        products = Product.objects.all()[:3]

    context = {
        'title': title,
        'menu_items': menu_items,
        'products': products,
        'product': product,
        'count': product_count,
        'total_cost': total_cost,

    }

    return render(request, 'mainapp/product.html', context)
