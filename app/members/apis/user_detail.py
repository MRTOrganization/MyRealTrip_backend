from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.views import APIView

from members.serializer import UserSerializer

User = get_user_model()

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
