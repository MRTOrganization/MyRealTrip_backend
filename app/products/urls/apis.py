from django.urls import path

from products import apis

urlpatterns = [
    path('product_list/', apis.ProductList.as_view()),
    path('product_list/<str:country>/<str:city>/', apis.ProductDetail.as_view()),
]
