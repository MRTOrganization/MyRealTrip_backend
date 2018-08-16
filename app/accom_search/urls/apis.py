from django.urls import path

urlpatterns = [
    path('', apis.AccomSearchList.as_view()),
    path('<int:pk>/', apis.AccomSearchDetail.as_view()),
]