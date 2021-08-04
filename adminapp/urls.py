from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    # path('users/create/', adminapp.user_create, name='user_create'),
    path('users/read/', adminapp.users, name='users'),
    # path('users/update/<int:pk>'),
    # path('users/delete/<int:pk>'),
    #
    # path('categories/create/'),
    # path('categories/read/', categories, name=categories),
    # path('categories/'),
    # path('categories/'),
    #
    # path('products/create/category/<int:pk/'),
    # path('products/read/catogory/<int:pk/'),
    # path('products/read/<int:pk>/'),
    # path('products/update/<int:pk>/'),
    # path('products/delete/<int:pk>/'),
]
