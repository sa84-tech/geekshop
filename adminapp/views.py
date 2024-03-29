from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, RedirectView

from adminapp.forms import ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm, ShopUserEditForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


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


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = ProductCategory
    template_name = 'adminapp/inc_category_update.html'
    form_class = ProductCategoryEditForm
    success_url = reverse_lazy('admin_staff:categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data()
        title = 'Категории/создание'
        context.update({'title': title})
        return context


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


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductCategory
    template_name = 'adminapp/inc_category_update.html'
    form_class = ProductCategoryEditForm
    success_url = reverse_lazy('admin_staff:categories')

    def get_context_data(self, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        title = 'Категории/редактирование'
        context.update({'title': title})
        return context


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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'adminapp/inc_product_update.html'
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


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'

    def get_context_data(self, *, object=None, **kwargs):
        # def get_context_data(self, *, object, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        title = 'продукты/подробнее'
        context.update({'title': title})
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'adminapp/inc_product_update.html'
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


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = not self.object.is_active
        self.object.save()

        return HttpResponseRedirect(reverse_lazy('admin_staff:products', args=[self.object.category.pk]))
