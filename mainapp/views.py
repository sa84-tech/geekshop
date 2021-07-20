from django.shortcuts import render

from .models import Product, ProductCategory, Contact


def index(request):
    title = 'каталог'
    menu_items = ProductCategory.objects.all()
    products = Product.objects.all()[:3]

    context = {
        'title': title,
        'menu_items': menu_items,
        'products': products,
    }

    return render(request, 'mainapp/products.html', context)
