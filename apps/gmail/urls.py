from django.urls import path

from .views import SendEmail


urlpatterns = [
    path('', SendEmail.as_view(), name="email"),
]
