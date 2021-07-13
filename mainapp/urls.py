from django.urls import path, include

from mainapp.views import index

urlpatterns = [
    path('', index),
]
