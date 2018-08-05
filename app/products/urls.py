from django.urls import path

from products import views

urlpatterns = [
    path('', views.city_list, name='city-list'),
    path('<str:country>/<str:city>/', views.ticket_list, name='ticket-list'),

]