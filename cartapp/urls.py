from django.urls import path

from cartapp.views import index, cart_edit, cart_add

app_name = 'cartapp'

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>', index, name='index'),
    path('add/<int:pk>/', cart_add, name='add'),
    path('edit/<int:pk>/<int:qtty>', cart_edit, name='edit'),
]
