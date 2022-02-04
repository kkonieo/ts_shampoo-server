from django.urls import include, path

from . import views

urlpatterns = [

    path("job/", views.job_list),
]
