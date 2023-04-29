from django.shortcuts import render

from cartapp.models import Cart
from mainapp.models import Product, Contact


def index(request):
    title = 'магазин'

    context = {
        'title': title,
        'popular_products': Product.get_popular_products(),
        'new_products': Product.get_new_products(),
    }

    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = 'контакты'
    contact_list = Contact.objects.all()

    context = {
        'title': title,
        'contact_list': contact_list,
    }

    print(request.resolver_match)
    return render(request, 'geekshop/contact.html', context)
