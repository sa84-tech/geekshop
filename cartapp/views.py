from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from cartapp.models import Cart
from mainapp.context_processors import get_total, get_count
from mainapp.models import Product


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

    cart_items = Cart.get_cart(request.user)

    context = {
        'title': title,
        'cart_items': cart_items,
    }

    return render(request, 'cartapp/cart.html', context)


@login_required
def cart_edit(request, pk, qty):
    print(pk, qty)
    cart = request.user.cart.get(product=pk)
    if qty > 0:
        cart.qty = int(qty)
        cart.save()
    else:
        cart.delete()

    total_cost = get_total(request.user)
    product_count = get_count(request.user)
    cart_items = Cart.get_cart(request.user)

    context = {
        'total_cost': total_cost,
        'count': product_count,
        'cart_items': cart_items,
    }

    result = render_to_string('cartapp/includes/inc_cart_items.html', context)

    return JsonResponse({'result': result, 'context': context})
