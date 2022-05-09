from django.urls import path

from cartapp.views import index, cart_edit

app_name = 'cartapp'

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>', index, name='index'),
    path('edit/<int:pk>/<int:qty>', cart_edit, name='edit'),
]
