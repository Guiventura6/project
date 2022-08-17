from django.shortcuts import render


def home(request):
    return render(request, 'products/home.html',
                  context={
                      'name': 'Name product',
                  })
