from django.shortcuts import render

from geekshop.utils import get_data


def index(request):

    title = 'каталог'

    menu_items = get_data('categories')

    products = get_data('products')[:3]

    context = {
        'title': title,
        'menu_items': menu_items,
        'products': products,
    }

    return render(request, 'mainapp/products.html', context)
