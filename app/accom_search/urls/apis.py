from django.urls import path

from accom_search import apis

urlpatterns = [
    path('', apis.AccomSearchList.as_view()),
    path('<int:pk>/', apis.AccomSearchDetail.as_view()),
]