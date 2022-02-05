from django.urls import include, path

from . import views

urlpatterns = [
    path("skill", views.user_skill_list),
    path("skill/<int:pk>/", views.user_skill_detail),
]
