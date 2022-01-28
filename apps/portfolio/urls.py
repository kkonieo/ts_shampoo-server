from django.urls import path, include
from . import views

app_name = "project"

urlpatterns = [
    path("<int:author>/project/", views.ProjectAPI.as_view(), name="project-list"),
    path("<int:author>/project/", views.ProjectDetailAPI.as_view(), name="project-detail"),
]
