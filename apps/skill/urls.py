from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.user_skill_list),
    path("<int:pk>", views.user_skill_detail),
]
