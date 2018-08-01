from django.urls import path

from members import views

urlpatterns = [
    path('', views.member_list, name='member-list')
]