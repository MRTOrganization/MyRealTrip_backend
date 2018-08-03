from django.urls import path, include

urlpatterns = [
    # View
    path('', include('config.urls.views')),
    # API
    path('api/', include('config.urls.apis')),
]
