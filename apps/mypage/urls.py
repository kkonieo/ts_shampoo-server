from django.urls import include, path

from . import views

urlpatterns = [

    path("profile", views.profile_list),
    path("profile/<int:pk>/", views.profile_detail),

    path("resume", views.resume_list),
    path("resume/<int:pk>/", views.resume_detail),

    path("award", views.award_list),
    path("award/<int:pk>/", views.award_detail),

    path("skill", views.user_skill_list),
    path("skill/<int:pk>/", views.user_skill_detail)
]
