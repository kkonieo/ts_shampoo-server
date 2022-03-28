from django.urls import path

from .views import UserEmail, SendEmail


urlpatterns = [
    path('<slug>', UserEmail.as_view(), name="user_email"),
    path('', SendEmail.as_view(), name="gmail"),
]
