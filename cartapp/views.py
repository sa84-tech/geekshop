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
    if product.qtty >= 1:
        cart, create = Cart.objects.get_or_create(user=user, product=product)
        if not create:
            cart.qtty += 1

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
def cart_edit(request, pk, qtty):
    print(f'controller: cart_edit, params - pk: {pk}, qtty: {qtty}')
    cart = request.user.cart.get(product=pk)
    # print(f'Product id: {cart.product.pk}: Prev qtty: {cart.product.qtty}')
    if qtty > 0:
        cart.qtty = int(qtty)
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
