from django.shortcuts import render

from mainapp.models import Product, Contact


def index(request):
    title = 'магазин'
    products = Product.objects.all()[3:]

    context = {
        'title': title,
        'products': products,
    }

    print(request.resolver_match)
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
