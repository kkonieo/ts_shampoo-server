from django.urls import include, path

from . import views

app_name = "project"

urlpatterns = [
    path("<int:author>/", views.ProjectAPI.as_view(), name="project-list"),
    path("<int:author>/<int:pk>/", views.ProjectDetailAPI.as_view(), name="project-detail"), # noqa : W503
    path("<int:author>/<int:pk>/projectDelete", views.ProjectDeleteAPI.as_view(), name='delete'), # noqa : W503
    path("<int:author>/<int:pk>/projectUpdate", views.ProjectUpdateAPI.as_view(), name='update'), # noqa : W503
]
