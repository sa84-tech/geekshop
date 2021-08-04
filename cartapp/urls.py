from django.urls import path

from cartapp.views import index, cart_add, cart_remove, cart_sub, cart_edit

app_name = 'cartapp'

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>', index, name='index'),
    # path('add/<int:pk>/', cart_add, name='add'),
    # path('sub/<int:pk>/', cart_sub, name='sub'),
    path('remove/<int:pk>/', cart_remove, name='remove'),
    path('edit/<int:pk>/<int:qty>', cart_edit, name='edit'),

]
