from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from cartapp.models import Cart
from mainapp.models import Product
from geekshop.views import get_count, get_total


def _add_cart(user, product_id):
    product = get_object_or_404(Product, pk=product_id)

    cart, create = Cart.objects.get_or_create(user=user, product=product)
    if not create:
        cart.qty += 1

    cart.save()
    return cart


@login_required
def index(request, pk=None):
    title = 'Корзина'
    if pk:
        _add_cart(request.user, pk)

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


@login_required
def cart_add(request, pk):
    _add_cart(request.user, pk)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    # return HttpResponseRedirect(reverse('cart:index'))


@login_required
def cart_remove(request, pk):

    cart = request.user.cart.get(product=pk)

    cart.delete()

    return HttpResponseRedirect(reverse('cart:index'))


@login_required
def cart_sub(request, pk):

    cart = request.user.cart.get(product=pk)

    if cart.qty > 1:
        cart.qty -= 1
        cart.save()
    else:
        cart.delete()

    return HttpResponseRedirect(reverse('cart:index'))


@login_required
def cart_edit(request, pk, qty):

    cart = request.user.cart.get(product=pk)
    cart.qty = int(qty)
    cart.save()

    cart_items = Cart.get_cart(request.user)

    context = {
        'cart_items': cart_items,
    }

    result = render_to_string('cartapp/includes/inc_cart_items.html', context)

    return JsonResponse({'result': result})
