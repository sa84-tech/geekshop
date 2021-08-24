from django.urls import path

from ordersapp.views import OrderList

app_name = 'ordersapp'

urlpatterns = [
    path('', OrderList.as_view(), name='orders_list'),
]
