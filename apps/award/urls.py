from django.urls import include, path

from .views import AwardListAPIView, AwardDetailAPIView, AwardAPIView

urlpatterns = [
    path("<slug>", AwardListAPIView.as_view(), name="award_get"),
    path("", AwardAPIView.as_view(), name="award_post"),
    path("<int:pk>/", AwardDetailAPIView.as_view(), name="award_update"),
]
