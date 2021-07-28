from django.urls import path

from mainapp.views import product_list

app_name = 'mainapp'

urlpatterns = [
    path('', product_list, name='index'),
    path('<int:pk>/', product_list, name='category'),
]
