
from django.urls import include, path

urlpatterns = [
    path('', include('products.urls.views')),
    path('api/', include('products.urls.apis')),
]
