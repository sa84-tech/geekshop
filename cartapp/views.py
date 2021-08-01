from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from cartapp.models import Cart
from mainapp.models import Product
from geekshop.views import get_count, get_total


def index(request):
    title = 'Корзина'
    product_count = get_count(request.user)
    total_cost = get_total(request.user)
    cart_items = Cart.get_cart(request.user)
    context = {
        'title': title,
        'count': product_count,
        'total_cost': total_cost,
        'cart_items': cart_items,
    }
    return render(request, 'cartapp/cart.html', context)


def cart_add(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('auth:login'))

    product = get_object_or_404(Product, pk=pk)

    cart, create = Cart.objects.get_or_create(user=request.user, product=product)
    if not create:
        cart.qty += 1

    cart.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def cart_remove(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('auth:login'))

    cart = get_object_or_404(user=request.user, product_id=pk)

    if cart.qty > 1:
        cart.qty -= 1
    else:
        cart.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
