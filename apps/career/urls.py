from django.urls import include, path

from .views import CareerListAPIView, CareerDetailAPIView, CareerAPIView

urlpatterns = [
    path("<slug>", CareerListAPIView.as_view(), name="career_get"),
    path("", CareerAPIView.as_view(), name="career_post"),
    path("<int:pk>/", CareerDetailAPIView.as_view(), name="career_update"),
]
