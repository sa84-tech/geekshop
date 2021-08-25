from django.urls import path

from ordersapp.views import OrderList, OrderItemsCreate, OrderDelete, OrderItemsUpdate, OrderRead

app_name = 'ordersapp'

urlpatterns = [
    path('', OrderList.as_view(), name='order_list'),
    path('create/', OrderItemsCreate.as_view(), name='order_create'),
    path('read/<int:pk>/', OrderRead.as_view(), name='order_read'),
    path('update/<int:pk/', OrderItemsUpdate.as_view(), name='order_update'),
    path('delete/<int:pk/', OrderDelete.as_view(), name='order_delete'),
]
