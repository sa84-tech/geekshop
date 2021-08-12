from django.urls import path

from authapp.views import login, logout, register, edit, verify

app_name = 'authapp'  # для функции include

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('verify/<str:email>/<activation_key>/', verify, name='verify')
]
