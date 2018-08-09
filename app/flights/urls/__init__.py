from django.urls import path, include

urlpatterns = [
    path('', include('flights.urls.views')),
    path('api/', include('flights.urls.apis')),
]