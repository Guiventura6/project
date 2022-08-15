from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'products/home.html')


def about(request):
    return HttpResponse('about 2')


def contact(request):
    return HttpResponse('contact 3')
