from django.shortcuts import render


def index(request):
    print(request.resolver_match)
    title = 'каталог'
    menu_items = [
        {'href': 'index', 'name': 'все'},
        {'href': 'index', 'name': 'дом'},
        {'href': 'index', 'name': 'офис'},
        {'href': 'index', 'name': 'модерн'},
        {'href': 'index', 'name': 'классика'},
    ]
    content = {
        'title': title,
        'menu_items': menu_items,
    }

    return render(request, 'mainapp/products.html', content)
