from django.contrib.auth import get_user_model, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from members.serializer import UserSerializer
from members.tokens import account_activation_token

User = get_user_model()


class UserList(APIView):
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(raw_password=request.data['password'])
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('members/user_activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = serializer.data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthToken(APIView):
    def post(self, request):
        # 전달받은 데이터에서 username, password추출

        # email = request.data.get('email')
        username = request.data.get('username')
        password = request.data.get('password')

        # authenticate가 성공한 경우
        user = authenticate(username=username, password=password)

        if user:
            # Token을 가져오거나 없으면 생성
            token, __ = Token.objects.get_or_create(user=user)
            # Response에 돌려줄 데이터
            data = {
                'token':token.key,
            }
            return Response(data)
        # authenticate에 실패한 경우
        raise AuthenticationFailed('인증정보가 올바르지 않습니다')
