from django.shortcuts import render

from authapp.models import ShopUser


def users(request):
    title = 'Панель управления/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'users': users_list,
    }

    return render(request, 'adminapp/users.html', context)
