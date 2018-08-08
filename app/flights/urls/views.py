from django.urls import path

from .. import views

urlpatterns = [
    path('', views.flight_list, name='flight-list'),
    path('<int:pk>/', views.flight_detail, name='flight-detail'),
]