from django.urls import path

from accommodations import views

urlpatterns = [
    path('', views.hotel_list, name='hotel-list'),
    path('<str:country>/<str:city>/', views.popularhotel_list, name='popularhotel-list'),
]