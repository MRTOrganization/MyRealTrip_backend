from django.conf.urls import url
from django.urls import path

from .. import views

app_name = 'members'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    path('facebook-login/', views.facebook_login, name='facebook-login'),
    path('mypage/', views.mypage, name='mypage'),
]
