from django.urls import path

import adminapp.views as adminapp
import adminapp.views_api as adminapp_api

app_name = 'adminapp'

urlpatterns = [
    path('api/', adminapp_api.index, name='index'),
    # path('users/create/', adminapp.user_create, name='user_create'),
    path('api/users/create/', adminapp_api.user_create, name='api_user_create'),
    # path('users/read/', adminapp.users, name='users'),
    path('api/users/read/', adminapp_api.users, name='api_users'),
    # path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('api/users/update/<int:pk>/', adminapp_api.user_update, name='api_user_update'),
    # path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),
    path('api/users/delete/<int:pk>/', adminapp_api.user_delete, name='api_user_delete'),

    # path('categories/create/', adminapp.category_create, name='category_create'),
    path('api/categories/create/', adminapp_api.category_create, name='api_category_create'),
    # path('categories/read/', adminapp.categories, name='categories'),
    path('api/categories/read/', adminapp_api.categories, name='api_categories'),
    # path('categories/update/<int:pk>/', adminapp.category_update, name='category_update'),
    path('api/categories/update/<int:pk>/', adminapp_api.category_update, name='api_category_update'),
    # path('categories/delete/<int:pk>/', adminapp.category_delete, name='category_delete'),
    path('api/categories/delete/<int:pk>/', adminapp_api.category_delete, name='api_category_delete'),

    path('api/products/create/category/<int:pk>/', adminapp_api.product_create, name='api_product_create'),
    # path('products/read/category/<int:pk>/', adminapp.products, name='products'),
    path('api/products/read/category/<int:pk>/', adminapp_api.products, name='api_products'),
    # path('products/read/<int:pk>/', adminapp.product_read, name='product_read'),
    path('api/products/update/<int:pk>/', adminapp_api.product_update, name='api_product_update'),
    # path('products/delete/<int:pk>/', adminapp.product_delete, name='product_delete'),
    path('api/products/delete/<int:pk>/', adminapp_api.product_delete, name='api_product_delete'),
]
