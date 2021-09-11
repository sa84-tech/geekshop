from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache import cache
from django.conf import settings

from .models import Product, ProductCategory


def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.filter(is_active=True)


def get_category(pk):
    if settings.LOW_CACHE:
        key = f'category_{pk}'
        category = cache.get(key)
        if category is None:
            category = get_object_or_404(ProductCategory, pk=pk)
            cache.set(key, category)
        return category
    else:
        return get_object_or_404(ProductCategory, pk=pk)


def get_products():
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True, category__is_active=True).select_related('category')


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product_{pk}'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Product, pk=pk)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Product, pk=pk)


def get_products_ordered_by_price():
    if settings.LOW_CACHE:
        key = 'products_orederd_by_price'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True, category__is_active=True).order_by('price')


def get_products_in_category_ordered_by_price(pk):
    if settings.LOW_CACHE:
        key = f'products_in_category_orederd_by_price_{pk}'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')


def product_list(request, pk=0, page=1):
    title = 'каталог'
    # menu_items = ProductCategory.objects.filter(is_active=True)
    menu_items = get_links_menu()

    if pk == 0:
        category = {
            'pk': 0,
            'name': 'Все',
        }
        # products = Product.objects.filter(is_active=True, category__is_active=True)
        products = get_products()
    else:
        # category = get_object_or_404(ProductCategory, pk=pk)
        # products = Product.objects.filter(category_id=pk, is_active=True, category__is_active=True)
        category = get_category(pk)
        products = get_products_in_category_ordered_by_price(pk)

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
        # product = get_object_or_404(Product, pk=pk)
        product = get_product(pk)
        products = list(Product.objects.filter(category_id=product.category)
                        .exclude(pk=pk)
                        .values_list('pk', 'image', 'category__name', 'name', 'short_desc', ))[:3]
    else:
        # products = Product.objects.all()[:3]
        products = get_products()[:3]
    context = {
        'title': title,
        'products': products,
        'product': product,
    }

    return render(request, 'mainapp/product.html', context)

