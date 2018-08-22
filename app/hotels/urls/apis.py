from django.urls import path

from hotels import views, apis

urlpatterns = [
    path('', apis.HotelList.as_view()),
    path('<str:country>/<str:city>/', apis.HotelDetail.as_view()),
    path('<str:country>/<str:city>/<int:pk>/', apis.HotelInfo.as_view()),
]
