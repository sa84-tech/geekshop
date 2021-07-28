from django.shortcuts import render

from .models import Product, ProductCategory
from cartapp.models import Cart


def product_list(request, pk=None):
    if request.user.is_authenticated:
        count = Cart.count(request.user)

    print(pk)
    title = 'каталог'
    menu_items = ProductCategory.objects.all()

    if pk:
        products = Product.objects.filter(category_id=pk)[:9]
    else:
        products = Product.objects.all()[:9]

    context = {
        'title': title,
        'menu_items': menu_items,
        'products': products,
        'count': count | 0,
    }

    return render(request, 'mainapp/product_list.html', context)


def product(request, pk=None):
    print(pk)
    title = 'каталог'
    menu_items = ProductCategory.objects.all()

    if pk:
        products = Product.objects.filter(category_id=pk)[:3]
    else:
        products = Product.objects.all()[:3]

    context = {
        'title': title,
        'menu_items': menu_items,
        'products': products,
    }

    return render(request, 'mainapp/product_list.html', context)
