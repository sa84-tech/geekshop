from django.contrib import auth
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm, ShopUserProfileEditForm
from authapp.models import ShopUser
from geekshop import settings


def login(request):
    title = 'вход'
    credentials = {}

    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST':
        login_form = ShopUserLoginForm(data=request.POST)
        if login_form.is_valid():
            credentials['username'] = request.POST['username']
            credentials['password'] = request.POST['password']

            user = auth.authenticate(**credentials)
            if user and user.is_active:
                auth.login(request, user)
                if 'next' in request.POST.keys():
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    return HttpResponseRedirect(reverse('index'))
    else:
        login_form = ShopUserLoginForm()

    context = {
        'title': title,
        'login_form': login_form,
        'next': next,
    }

    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])

    subject = f'Подтверждение регистрации на сайте {settings.DOMAIN_NAME}'

    message = f'Для подтверждение учетной записи {user.username} на сайте {settings.DOMAIN_NAME}' \
              f' - пройдите по ссылке: {settings.DOMAIN_NAME}{verify_link}'

    html_message = f'<div>Для подтверждение учетной записи {user.username} на сайте {settings.DOMAIN_NAME}' \
                   f' - пройдите по ссылке: <a href="{settings.DOMAIN_NAME}{verify_link}">Активировать</a></div>'

    return send_mail(
        subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False, html_message=html_message
    )


def verify(request, email, activation_key):

    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired:
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'authapp/verification.html')
        else:
            print(f'Activation key error. User: ({user.username})')
            return render(request, 'authapp/verification.html')
    except Exception as error:
        print(f'Error: {error.args}')
        return HttpResponseRedirect(reverse('index'))


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        print('******************', register_form.is_valid())
        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                print('сообщение отправлено')
                return render(
                    request,
                    'authapp/registration_result.html',
                    {'title': title, 'user': user, 'success': True}
                )
            else:
                print('сообщение не отправлено')
                return render(
                    request,
                    'authapp/registration_result.html',
                    {'title': title, 'user': user, 'success': False}
                )
    else:
        register_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'register_form': register_form
    }
    return render(request, 'authapp/register.html', context)


def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        profile_form = ShopUserProfileEditForm(request.POST, instance=request.user.shopuserprofile)
        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)
        profile_form = ShopUserProfileEditForm(instance=request.user.shopuserprofile)

    context = {
        'title': title,
        'edit_form': edit_form,
        'profile_form': profile_form,
    }

    return render(request, 'authapp/edit.html', context)
