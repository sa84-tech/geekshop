from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin

from adminapp.forms import ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm, ShopUserEditForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product

# @user_passes_test(lambda u: u.is_superuser)
# def user_create(request):
#     title = 'Пользователи/создание'
#
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:users'))
#
#     else:
#         user_form = ShopUserRegisterForm()
#
#     context = {
#         'title': title,
#         'user_form': user_form,
#     }
#
#     return render(request, 'adminapp/user_update.html', context)


class UserCreateView(LoginRequiredMixin, CreateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    form_class = ShopUserRegisterForm
    success_url = reverse_lazy('admin_staff:users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data()
        title = 'Пользователи/создание'
        context.update({'title': title})
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'Панель управления/пользователи'
#
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#     context = {
#         'title': title,
#         'users': users_list,
#     }
#
#     return render(request, 'adminapp/users.html', context)


class UserListView(LoginRequiredMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    def get_queryset(self):
        return ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data()
        title = 'админка / пользователи'
        context.update({'title': title})
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def user_update(request, pk):
#     title = 'Пользователи/редактирование'
#
#     cur_user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         user_form = ShopUserEditForm(request.POST, request.FILES, instance=cur_user)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:users'))
#
#     else:
#         user_form = ShopUserEditForm(instance=cur_user)
#
#     context = {
#         'title': title,
#         'user_form': user_form,
#     }
#
#     return render(request, 'adminapp/user_update.html', context)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    form_class = ShopUserEditForm
    success_url = reverse_lazy('admin_staff:users')

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        title = 'Пользователи/редактирование'
        context.update({'title': title})
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def user_delete(request, pk):
#     title = 'пользователи/удаление'
#
#     user = get_object_or_404(ShopUser, pk=pk)
#
#     print(request.method, user)
#
#     if request.method == 'POST':
#         user.is_active = False
#         user.save()
#         return HttpResponseRedirect(reverse('admin_staff:users'))
#
#     context = {
#         'title': title,
#         'user': user,
#     }
#
#     return render(request, 'adminapp/user_delete.html', context)


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = ShopUser
    template_name = 'adminapp/object_delete.html'
    success_url = reverse_lazy('admin_staff:users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = not self.object.is_active
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(UserDeleteView, self).get_context_data(**kwargs)
        title = 'Пользователи/удаление' if self.get_object().is_active else 'Пользователи/восстановление'
        url_values = {'get': 'admin_staff:users', 'post': 'admin_staff:user_delete'}
        context.update({'title': title, 'url_values': url_values})
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#     title = 'Категории/создание'
#
#     if request.method == 'POST':
#         category_form = ProductCategoryEditForm(request.POST, request.FILES)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:categories'))
#
#     else:
#         category_form = ProductCategoryEditForm()
#
#     context = {
#         'title': title,
#         'category_form': category_form,
#     }
#
#     return render(request, 'adminapp/category_update.html', context)


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    form_class = ProductCategoryEditForm
    success_url = reverse_lazy('admin_staff:categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data()
        title = 'Категории/создание'
        context.update({'title': title})
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def categories(request):
#     title = 'Панель управления/категории'
#
#     categories_list = ProductCategory.objects.all()
#
#     print('***********', list(categories_list.values()))
#
#     context = {
#         'title': title,
#         'objects': categories_list,
#     }
#
#     return render(request, 'adminapp/categories.html', context)


class CategoryListView(LoginRequiredMixin, ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    def get_queryset(self):
        print(self.kwargs)
        return ProductCategory.objects.all().order_by('-is_active', 'name')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data()
        title = 'Панель администрирование/категории'
        context.update({'title': title})
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#     title = 'Категории/редактирование'
#
#     cur_category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         category_form = ProductCategoryEditForm(request.POST, instance=cur_category)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:categories'))
#
#     else:
#         category_form = ProductCategoryEditForm(instance=cur_category)
#
#     context = {
#         'title': title,
#         'category_form': category_form,
#     }
#
#     return render(request, 'adminapp/category_update.html', context)


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    form_class = ProductCategoryEditForm
    success_url = reverse_lazy('admin_staff:categories')

    def get_context_data(self, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        title = 'Категории/редактирование'
        context.update({'title': title})
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#     title = 'Категории / удаление'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         category.is_active = False
#         category.save()
#         return HttpResponseRedirect(reverse('admin_staff:categories'))
#
#     context = {
#         'title': title,
#         'category': category,
#     }
#
#     return render(request, 'adminapp/category_delete.html', context)


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = ProductCategory
    template_name = 'adminapp/object_delete.html'
    success_url = reverse_lazy('admin_staff:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = not self.object.is_active
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(CategoryDeleteView, self).get_context_data(**kwargs)
        title = 'Категории/удаление' if self.get_object().is_active else 'Категории/восстановление'
        url_values = {'get': 'admin_staff:categories', 'post': 'admin_staff:category_delete'}
        context.update({'title': title, 'url_values': url_values})
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def product_create(request, pk):
#     title = 'Продукты/создание'
#     category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         product_form = ProductEditForm(request.POST, request.FILES)
#         if product_form.is_valid():
#             product_form.save()
#             return HttpResponseRedirect(reverse('adminapp:products', args=[pk]))
#
#     else:
#         product_form = ProductEditForm(initial={'category': category})
#
#     context = {
#         'title': title,
#         'update_form': product_form,
#         'category': category,
#     }
#
#     return render(request, 'adminapp/product_update.html', context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    form_class = ProductEditForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        edit_form = ProductEditForm(request.POST, request.FILES, instance=self.object)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin_staff:products', args=[self.object.pk]))

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        title = 'Продукты/редактирование'
        context.update({'title': title})
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def products(request, pk):
#     title = 'Панель администрирование/продукт'
#     category = get_object_or_404(ProductCategory, pk=pk)
#     products_list = Product.objects.filter(category__pk=pk).order_by('name')
#
#     context = {
#         'title': title,
#         'category': category,
#         'objects': products_list,
#     }
#
#     return render(request, 'adminapp/products.html', context)


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'adminapp/products.html'

    def get_queryset(self):
        print(self.kwargs)
        return Product.objects.filter(category__pk=self.kwargs['pk']).order_by('-is_active', 'name')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        title = 'Панель администрирование/продукт'
        category = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
        context.update({'title': title, 'category': category})
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def product_read(request, pk):
#     title = 'продукты/подробнее'
#     product = get_object_or_404(Product, pk=pk)
#
#     context = {
#         'title': title,
#         'object': product,
#     }
#
#     return render(request, 'adminapp/product_read.html', context)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'

    def get_context_data(self, *, object=None, **kwargs):
        # def get_context_data(self, *, object, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        title = 'продукты/подробнее'
        context.update({'title': title})
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def product_update(request, pk):
#     title = 'Продукты/реадктирование'
#
#     cur_product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         edit_form = ProductEditForm(request.POST, request.FILES, instance=cur_product)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('adminapp:product_update', args=[cur_product.pk]))
#
#     else:
#         edit_form = ProductEditForm(instance=cur_product)
#
#     context = {
#         'title': title,
#         'update_form': edit_form,
#         'category': cur_product.category,
#     }
#
#     return render(request, 'adminapp/product_update.html', context)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    form_class = ProductEditForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        edit_form = ProductEditForm(request.POST, request.FILES, instance=self.object)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin_staff:product_update', args=[self.object.category.pk]))

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        title = 'Продукты/редактирование'
        context.update({'title': title})
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request, pk):
#     title = 'Продукты/удаление'
#
#     cur_product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         cur_product.is_active = False
#         cur_product.save()
#         return HttpResponseRedirect(reverse('adminapp:products', args=[cur_product.category.pk]))
#
#     context = {
#         'title': title,
#         'product': cur_product,
#     }
#
#     return render(request, 'adminapp/product_delete.html', context)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = not self.object.is_active
        self.object.save()

        return HttpResponseRedirect(reverse_lazy('admin_staff:products', args=[self.object.category.pk]))
