from django.urls import path

from accommodations import apis

urlpatterns = [
    path('', apis.AccommodationsList.as_view()),
    path('<str:country>/<str:city>/', apis.AccommodationsDetail.as_view()),
]
