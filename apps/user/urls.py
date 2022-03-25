from django.urls import path

from .views import (GoogleSocialAuthView, LogoutAPIView, UserAPIView,
                    UserTokenRefreshView, DeleteUserView)

urlpatterns = [
    path("register/", GoogleSocialAuthView.as_view(), name="register"),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path("profile/", UserAPIView.as_view(), name='profile'),
    path("refresh/", UserTokenRefreshView.as_view(), name="refresh"),
    path("delete/", DeleteUserView.as_view(), name="delete"),
]
