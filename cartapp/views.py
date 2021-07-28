from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def index(request):
    print('index')
    return HttpResponseRedirect(reverse('index'))
