from django.urls import path

from products.views import product_list, popular_city_list

urlpatterns = [
    path('', popular_city_list, name='popular-city-list'),
    path('product_list/', product_list, name='product-list'),
]
