from django.urls import path, include

urlpatterns = [
    path('', include('members.urls.views')),
    path('api/', include('members.urls.apis')),
]