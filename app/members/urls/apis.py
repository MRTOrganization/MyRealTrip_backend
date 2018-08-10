from django.urls import path

from .. import apis

urlpatterns = [
    path('', apis.UserList.as_view()),
    path('auth-token/', apis.AuthToken.as_view()),
    path('<int:pk>/', apis.UserDetail.as_view()),
    path('profile/', apis.UserProfile.as_view()),
]
