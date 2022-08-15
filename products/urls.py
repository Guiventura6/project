from django.urls import path

from products.views import about, contact, home

urlpatterns = [
    path('', home),
    path('about/', about),
    path('contact/', contact),
]
