from django.urls import path

from hotels import views

urlpatterns = [
    path('', views.city_list, name='city-list'),
    path('<str:country>/<str:city>/', views.koreanhotel_list, name='koreanhotel-list'),
    path('<str:country>/<str:city>/<int:pk>/', views.koreanhotel_detail, name='koreanhotel-detail'),
]