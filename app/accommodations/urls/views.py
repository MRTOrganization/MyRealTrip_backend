from django.urls import path

from accommodations import views

urlpatterns = [
    path('', views.country_list, name='country-list'),
    path('<str:country>/<str:city>/', views.popularhotel_list, name='popularhotel-list'),
]