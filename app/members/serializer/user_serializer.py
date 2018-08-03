from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    img_profile = serializers.ImageField(required=False, allow_empty_file=True)

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

    def validate_password(self, password):
        password2 = self.initial_data.get('password2')

        if not password == password2:
            raise serializers.ValidationError('비밀번호가 일치하지 않습니다.')

        errors = dict()

        try:
            validate_password(password=password)

        except ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return password

    def create(self, validate_data):
        password = validate_data['password']

        user = User.objects.create_user(
            username=validate_data['username'],
            first_name=validate_data['first_name'],
            email=validate_data['email'],
            phone_number=validate_data['phone_number'],
        )

        if 'img_profile' in validate_data:
            user.img_profile = validate_data['img_profile']

        user.set_password(password)
        user.save()
        return user

