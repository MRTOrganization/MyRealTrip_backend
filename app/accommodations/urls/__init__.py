from django.urls import path, include

urlpatterns = [
    path('', include('accommodations.urls.views')),
    path('api/', include('accommodations.urls.apis')),
]