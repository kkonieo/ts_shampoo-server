from django.urls import include, path

from . import views

app_name = "project"

urlpatterns = [
    path("<int:author>/", views.ProjectAPI.as_view(), name="project-list"),
    path("<int:author>/<int:pk>/", views.ProjectDetailAPI.as_view(), name="project-detail"),  # noqa : W503
]
