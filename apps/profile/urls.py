from django.urls import include, path

from .views import ProfileRetrieveAPIView, ProfileAPIView

urlpatterns = [
    path("<slug>", ProfileRetrieveAPIView.as_view(), name="profile"),
    path("", ProfileAPIView.as_view(), name="profile"),
]
