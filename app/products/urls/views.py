from django.urls import path

from products import views

urlpatterns = [
    path('', views.popular_city_list, name='popular-city-list'),
    path('search_result/', views.product_search, name='product-search'),
    path('product_list/', views.product_list, name='product-list'),
    path('product_list/<str:country>/<str:city>/', views.product_city_content, name='product-city-content'),
    path('product_list/<str:country>/<str:city>/<int:pk>/', views.product_detail, name='product-detail'),
]
