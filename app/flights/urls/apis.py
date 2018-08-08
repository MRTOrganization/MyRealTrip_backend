from django.urls import path

from .. import apis

urlpatterns = [
    path('', apis.FlightList.as_view()),
    path('<int:pk>/', apis.FlightDetail.as_view()),
]