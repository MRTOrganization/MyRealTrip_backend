from django.urls import path, include

urlpatterns = [
    path('', include('accom_search.urls.views')),
    path('api/', include('accom_search.urls.apis')),
]