from django.shortcuts import render


def index(request):
    title = 'магазин'
    content = {
        'title': title
    }

    print(request.resolver_match)
    return render(request, 'geekshop/index.html', content)


def contacts(request):
    title = 'контакты'
    content = {
        'title': title
    }

    print(request.resolver_match)
    return render(request, 'geekshop/contact.html', content)
