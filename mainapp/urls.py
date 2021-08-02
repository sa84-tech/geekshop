from django.urls import path

from mainapp.views import product_list, product_details

app_name = 'mainapp'

urlpatterns = [
    path('', product_list, name='index'),
    path('category/<int:pk>/', product_list, name='category'),
    path('product/<int:pk>/', product_details, name='product'),
]
