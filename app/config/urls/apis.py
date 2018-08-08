from django.urls import path, include

urlpatterns = [
    path('members/', include('members.urls.apis')),
    path('flights/', include('flights.urls.apis')),
]