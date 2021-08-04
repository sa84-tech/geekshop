from django.shortcuts import render

from cartapp.models import Cart
from mainapp.models import Product, Contact


def get_count(user):
    product_count = 0
    if user.is_authenticated:
        product_count = Cart.count(user)
    return product_count


def get_total(user):
    total_cost = 0
    if user.is_authenticated:
        total_cost = Cart.total(user)
    return total_cost


def index(request):
    title = 'магазин'
    popular_products = Product.objects.all().order_by('price')[:3]
    new_products = Product.objects.all().order_by('-id')[:3]
    product_count = get_count(request.user)
    total_cost = get_total(request.user)

    context = {
        'title': title,
        'popular_products': popular_products,
        'new_products': new_products,
        'count': product_count,
        'total_cost': total_cost,
    }

    # print(request.resolver_match)
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = 'контакты'
    contact_list = Contact.objects.all()
    product_count = get_count(request.user)
    total_cost = get_total(request.user)

    context = {
        'title': title,
        'contact_list': contact_list,
        'count': product_count,
        'total_cost': total_cost,
    }

    print(request.resolver_match)
    return render(request, 'geekshop/contact.html', context)
