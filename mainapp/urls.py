from django.urls import path
from django.views.decorators.cache import cache_page

from mainapp.views import product_list, product_details, product_list_ajax

app_name = 'mainapp'

urlpatterns = [
    path('', product_list, name='index'),
    path('category/<int:pk>/', product_list, name='category'),
    path('category/<int:pk>/ajax/', cache_page(3600)(product_list_ajax)),
    path('category/<int:pk>/page/<int:page>/', product_list, name='page'),
    path('category/<int:pk>/page/<int:page>/ajax/', cache_page(3600)(product_list_ajax)),
    path('product/<int:pk>/', product_details, name='product'),
]
