from django.urls import path, include

urlpatterns = [
    path('members/', include('members.urls.apis')),
    path('flights/', include('flights.urls.apis')),
    path('khotels/', include('hotels.urls.apis')),
    path('products/', include('products.urls.apis')),
    path('accommodations/', include('accommodations.urls.apis')),
    path('accom-search/', include('accom_search.urls.apis')),
]
