from django.shortcuts import render

from geekshop.utils import get_data


def index(request):
    title = 'магазин'

    products = get_data('products')[-2:]

    context = {
        'title': title,
        'products': products,
    }

    print(request.resolver_match)
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = 'контакты'

    contact_list = get_data('contacts')

    context = {
        'title': title,
        'contact_list': contact_list,
    }

    print(request.resolver_match)
    return render(request, 'geekshop/contact.html', context)
