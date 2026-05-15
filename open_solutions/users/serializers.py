from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model


User = get_user_model()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True
    )
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            username=email,
            password=password
        )
        if not user:
            raise serializers.ValidationError(
                'Неверный email или пароль'
            )
        attrs['user'] = user
        return attrs

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True
    )

    password2 = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User

        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'middle_name',
            'company',
            'position',
            'password',
            'password2',
        )

    def validate(self, attrs):

        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                'Пароли не совпадают'
            )

        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')

        user = User.objects.create_user(
            **validated_data
        )

        return user