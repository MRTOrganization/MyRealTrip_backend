from django.urls import path

from .. import views

urlpatterns = [
    path('', views.accom_search_list, name='accom-search-list'),
    path('<int:pk>/', views.accom_search_detail, name='accom-search-detail'),
]