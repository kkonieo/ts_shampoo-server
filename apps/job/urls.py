from django.urls import include, path

from .views import JobListAPIView

urlpatterns = [
    path("", JobListAPIView.as_view()),
]
