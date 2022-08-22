from django.shortcuts import render


def home(request):
    return render(request, 'products/pages/home.html',
                  context={
                      'name': 'Product Name',
                  })
