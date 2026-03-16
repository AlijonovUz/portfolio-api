import re

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff']
        read_only_fields = ['id', 'is_active', 'is_staff']

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError("Bu elektron pochta allaqachon ishlatilmoqda.")
        return value


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(min_length=8, max_length=128, write_only=True,
                                         style={'input_type': 'password'})
    new_password = serializers.CharField(min_length=8, max_length=128, write_only=True,
                                         style={'input_type': 'password'})
    confirm_new_password = serializers.CharField(min_length=8, max_length=128, write_only=True,
                                                 style={'input_type': 'password'})

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Eski parol noto'g'ri.")
        return value

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_new_password']:
            raise serializers.ValidationError({
                'password': "Yangi parol maydonlari mos kelmadi."
            })
        if attrs['old_password'] == attrs['new_password']:
            raise serializers.ValidationError({
                'password': "Yangi parol eskisidan farq qilishi kerak."
            })

        try:
            validate_password(attrs['new_password'], user=self.context['request'].user)
        except ValidationError as e:
            raise serializers.ValidationError({'password': e.messages})

        return attrs

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data: dict = super().validate(attrs)

        user = self.user

        data["user"] = {
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_active": user.is_active,
            "is_staff": user.is_staff
        }

        return data


class MyTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data: dict = super().validate(attrs)

        refresh = RefreshToken(attrs["refresh"])
        user_id = refresh.get("user_id")

        try:
            user = User.objects.get(id=user_id)
            data["user"] = {
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "is_active": user.is_active,
                "is_staff": user.is_staff
            }
        except User.DoesNotExist:
            pass

        return data
