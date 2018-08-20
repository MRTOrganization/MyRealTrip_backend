from django.urls import path, include

urlpatterns = [
    path('', include('hotels.urls.views')),
    path('api/', include('hotels.urls.apis')),
]
