from django.db import connection
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin

from adminapp.forms import ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm, ShopUserEditForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


def db_profile_by_type(prefix, type, queries):
    update_queries = list(filter(lambda x: type in x['sql'], queries))
    print(f'db_profile {type} for {prefix}:')
    [print(query['sql']) for query in update_queries]


@receiver(pre_save, sender=ProductCategory)
def product_is_active_update_productcategory_save(sender, instance, **kwargs):
    if instance.pk:
        if instance.is_active:
            instance.product_set.update(is_active=True)
        else:
            instance.product_set.update(is_active=False)
        db_profile_by_type(sender, 'UPDATE', connection.queries)


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/base.html', {'title': 'Панель администрироваия'})


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'Пользователи/создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return JsonResponse({'is_valid': user_form.is_valid()})
    else:
        user_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'user_form': user_form,
    }

    result = render_to_string('adminapp/includes/inc_user_update.html', context, request=request)
    return JsonResponse({'result': result})


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'Панель управления/пользователи'
    print(request)
    users_list = list(ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username').values())

    context = {
        'title': title,
        'objects': users_list,
    }

    return JsonResponse(context)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'Пользователи/редактирование'

    cur_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user_form = ShopUserEditForm(request.POST, request.FILES, instance=cur_user)
        print(user_form.is_valid())
        if user_form.is_valid():
            user_form.save()
            return JsonResponse({'is_valid': user_form.is_valid()})

    else:
        user_form = ShopUserEditForm(instance=cur_user)

    context = {
        'title': title,
        'edit_user_id': pk,
        'user_form': user_form,
    }

    result = render_to_string('adminapp/includes/inc_user_update.html', context, request=request)

    return JsonResponse({'result': result})


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'пользователи/удаление'

    user = get_object_or_404(ShopUser, pk=pk)
    user.is_active = not user.is_active
    user.save()

    users_list = list(ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username').values())

    context = {
        'title': title,
        'objects': users_list,
    }

    return JsonResponse(context)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = 'Категории/создание'

    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return JsonResponse({'is_valid': category_form.is_valid()})

    else:
        category_form = ProductCategoryEditForm()

    context = {
        'title': title,
        'form': category_form,
    }

    result = render_to_string('adminapp/includes/inc_category_update.html', context, request=request)

    return JsonResponse({'result': result})


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'Панель управления/категории'

    categories_list = list(ProductCategory.objects.all().order_by('-is_active', 'name').values())

    context = {
        'title': title,
        'objects': categories_list,
    }

    return JsonResponse(context)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    title = 'Категории/редактирование'

    cur_category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, instance=cur_category)
        if category_form.is_valid():
            category_form.save()
            return JsonResponse({'is_valid': category_form.is_valid()})

    else:
        category_form = ProductCategoryEditForm(instance=cur_category)

    context = {
        'title': title,
        'edit_category_id': pk,
        'form': category_form,
    }

    result = render_to_string('adminapp/includes/inc_category_update.html', context, request=request)

    return JsonResponse({'result': result})


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    title = 'Категории / удаление'

    category = get_object_or_404(ProductCategory, pk=pk)
    category.is_active = not category.is_active
    category.save()

    categories_list = list(ProductCategory.objects.all().order_by('-is_active', 'name').values())

    context = {
        'title': title,
        'objects': categories_list,
    }

    return JsonResponse(context)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    title = 'Продукты/создание'
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        print(product_form.is_valid())
        if product_form.is_valid():
            product_form.save()
            print('***************', pk)
            return JsonResponse({'is_valid': product_form.is_valid(), 'category': pk})

    else:
        product_form = ProductEditForm(initial={'category': category})

    context = {
        'title': title,
        'form': product_form,
        'category': category,
    }

    result = render_to_string('adminapp/includes/inc_product_update.html', context, request=request)

    return JsonResponse({'result': result})


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'Панель администрирование/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)

    products_list = list(Product.objects.filter(category__pk=pk).order_by('-is_active', 'name').values())

    objects = {
        'products_list': products_list,
        'category': {'id': category.id, 'name': category.name},
    }

    context = {
        'title': title,
        'objects': objects,
    }

    return JsonResponse(context)


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = 'Продукты/реадктирование'

    cur_product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=cur_product)
        print(edit_form.is_valid())
        if edit_form.is_valid():
            edit_form.save()
            return JsonResponse({'is_valid': edit_form.is_valid(), 'category': cur_product.category.pk})

    else:
        edit_form = ProductEditForm(instance=cur_product)

    context = {
        'title': title,
        'form': edit_form,
        'product_id': cur_product.pk,
    }

    result = render_to_string('adminapp/includes/inc_product_update.html', context, request=request)

    return JsonResponse({'result': result})


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    title = 'Продукты / удаление'

    product = get_object_or_404(Product, pk=pk)
    product.is_active = not product.is_active
    product.save()

    category = get_object_or_404(ProductCategory, pk=product.category.pk)

    products_list = list(Product.objects.filter(category=category.pk).order_by('-is_active', 'name').values())

    objects = {
        'products_list': products_list,
        'category': {'id': category.pk, 'name': category.name},
    }

    context = {
        'title': title,
        'objects': objects,
    }

    return JsonResponse(context)
