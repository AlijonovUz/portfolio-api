from django.urls import path

from .views import *

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
    path("login/", MyTokenObtainPairView.as_view(), name='login'),
    path("refresh/", MyTokenRefreshView.as_view(), name='refresh'),
]
