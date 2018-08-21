from django.urls import path

from products import apis

urlpatterns = [
    path('popular_city/', apis.PopularCityList.as_view()),
    path('product_city_list/', apis.ProductCityList.as_view()),
    path('product_list/', apis.ProductList.as_view()),
    path('product_search/<str:keyword>/', apis.ProductSearch.as_view()),
    path('product_list/<str:country>/<str:city>/', apis.ProductDetail.as_view()),
    # path('product_list/<str:country>/<str:city>/ticket/', apis.ProductTicket),
]
