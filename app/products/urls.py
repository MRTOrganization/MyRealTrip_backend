from django.urls import path

from products.views import product_list

urlpatterns = [
    path('', product_list, name='product-list'),
]
