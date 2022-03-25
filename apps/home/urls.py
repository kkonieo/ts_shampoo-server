from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.HomeListAPIView.as_view()),
]
