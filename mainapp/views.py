from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Product, ProductCategory


def product_list(request, pk=0, page=1):
    title = 'каталог'
    menu_items = ProductCategory.objects.filter(is_active=True)

    if pk == 0:
        category = {
            'pk': 0,
            'name': 'Все',
        }
        products = Product.objects.filter(is_active=True, category__is_active=True)
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = Product.objects.filter(category_id=pk, is_active=True, category__is_active=True)

    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': title,
        'menu_items': menu_items,
        'products': products_paginator,
        'category': category,
    }

    return render(request, 'mainapp/product_list.html', context)


def product_details(request, pk=None):
    title = 'каталог'

    if pk:
        product = get_object_or_404(Product, pk=pk)
        products = list(Product.objects.filter(category_id=product.category)
                        .exclude(pk=pk)
                        .values_list('pk', 'image', 'category__name', 'name', 'short_desc', ))[:3]
        print(products)
    else:
        products = Product.objects.all()[:3]

    context = {
        'title': title,
        'products': products,
        'product': product,
    }

    return render(request, 'mainapp/product.html', context)
