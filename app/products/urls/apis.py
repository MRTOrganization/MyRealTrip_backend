from django.urls import path

from products import apis

urlpatterns = [
    path('popular_city/', apis.PopularCityList.as_view()),
    path('product_list/', apis.ProductList.as_view()),
    path('product_list/guides/', apis.ProductListGuide.as_view()),
    path('product_list/tickets/', apis.ProductListTicket.as_view()),
    path('product_list/activities/', apis.ProductListActivity.as_view()),
    path('product_list/snapshot/', apis.ProductListSnapShot.as_view()),
    path('product_list/fun/', apis.ProductListFun.as_view()),
    path('product_list/convenience/', apis.ProductListConvenience.as_view()),
    path('product_search/<str:keyword>/', apis.ProductSearch.as_view()),
    path('product_list/<str:country>/<str:city>/', apis.ProductDetail.as_view()),
]
