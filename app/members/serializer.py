from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'email',
            'first_name',
            'phone_number',
            'img_profile',
            'introduce',
            'password',
            'password2',
            'is_facebook_user',
        )
