from django.urls import path

from cartapp.views import index, cart_add, cart_remove

app_name = 'cartapp'

urlpatterns = [
    path('', index, name='view'),
    path('add/<int:pk>/', cart_add, name='add'),
    path('remove/<int:pk>/', cart_remove, name='remove'),
]
