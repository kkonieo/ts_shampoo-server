from django.urls import path

from .views import GoogleSocialAuthView, LogoutAPIView, UserAPIView

urlpatterns = [
    path("register/", GoogleSocialAuthView.as_view(), name="register"),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path("profile/", UserAPIView.as_view(), name='profile')
]
