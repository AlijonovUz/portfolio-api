from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

from .serializers import *

@extend_schema(tags=['Account'])
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


@extend_schema(tags=["Account"])
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'message': 'Parol muvaffaqiyatli yangilandi.'
        }, status=status.HTTP_200_OK)


@extend_schema(tags=["Auth"])
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@extend_schema(tags=["Auth"])
class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer
