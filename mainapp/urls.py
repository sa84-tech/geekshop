from django.urls import path

from mainapp.views import index

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', index, name='category'),
]
