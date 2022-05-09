from cartapp.models import Cart


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


def cart(request):
    product_count = get_count(request.user)
    total_cost = get_total(request.user)

    return {
        'count': product_count,
        'total_cost': total_cost,
    }
