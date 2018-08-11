from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import generics, status
from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from members.serializer import UserSerializer

User = get_user_model()

class UserDetail(APIView):
    def get_obejct(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_obejct(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_obejct(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_obejct(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserProfile(APIView):
    # URL: /api/members/profile/
    def get(self, request):
        if request.user.is_authenticated:
            return Response(UserSerializer(request.user).data)
        raise NotAuthenticated('로그인 되어있지 않습니다.')