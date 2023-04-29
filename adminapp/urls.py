from django.urls import path

import adminapp.views as adminapp
import adminapp.views_api as adminapp_api

app_name = 'adminapp'

urlpatterns = [
    path('api/', adminapp_api.index, name='index'),
    path('api/users/create/', adminapp_api.user_create, name='api_user_create'),
    path('api/users/read/', adminapp_api.users, name='api_users'),
    path('api/users/update/<int:pk>/', adminapp_api.user_update, name='api_user_update'),
    path('api/users/delete/<int:pk>/', adminapp_api.user_delete, name='api_user_delete'),

    path('api/categories/create/', adminapp_api.category_create, name='api_category_create'),
    path('api/categories/read/', adminapp_api.categories, name='api_categories'),
    path('api/categories/update/<int:pk>/', adminapp_api.category_update, name='api_category_update'),
    path('api/categories/delete/<int:pk>/', adminapp_api.category_delete, name='api_category_delete'),

    path('api/products/create/category/<int:pk>/', adminapp_api.product_create, name='api_product_create'),
    path('api/products/read/category/<int:pk>/', adminapp_api.products, name='api_products'),
    path('api/products/update/<int:pk>/', adminapp_api.product_update, name='api_product_update'),
    path('api/products/delete/<int:pk>/', adminapp_api.product_delete, name='api_product_delete'),
]
