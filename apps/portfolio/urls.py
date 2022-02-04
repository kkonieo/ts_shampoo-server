from django.urls import path, include
from . import views

app_name = "project"

urlpatterns = [
    path("<int:author>/", views.ProjectAPI.as_view(), name="project-list"),
    path("<int:author>/<int:pk>/", views.ProjectDetailAPI.as_view(), name="project-detail"),
    path("<int:author>/<int:pk>/projectDelete", views.ProjectDeleteAPI.as_view(), name='delete'),
    path("<int:author>/<int:pk>/projectUpdate", views.ProjectUpdateAPI.as_view(), name='update'),
]
