from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

User = get_user_model()


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    password2 = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            'password',
            'passwords',
        )

    def validate_password(self, password):
        password2 = self.initial_data.get('password2')

        if not password == password2:
            raise ValidationError('비밀번호가 일치하지 앟습니다.')
        errors = dict()

        try:
            validate_password(password=password)
        except ValidationError as e:
            errors['password'] = list(e.messages)
            print(errors)

        if errors:
            raise serializers.ValidationError(errors)

        return password

    def update(self, instance, validate_data):
        instance.set_password(validate_data['password'])
        instance.save()

        return instance






