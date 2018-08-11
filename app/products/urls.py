from django.urls import path

from products.views import product_list, popular_city_list, product_city_content

urlpatterns = [
    path('', popular_city_list, name='popular-city-list'),
    path('product_list/', product_list, name='product-list'),
    path('product_list/<str:country>/<str:city>/', product_city_content, name='product-city-content'),
]
