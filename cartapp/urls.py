from django.urls import path

from cartapp.views import index

app_name = 'authapp'  # для функции include

urlpatterns = [
    path('', index, name='cart'),
]
