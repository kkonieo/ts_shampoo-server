from django.urls import include, path

from .views import UserSkillListAPIView, UserSkillDetailAPIView, UserSkillAPIView, SkillListAPIView # noqa : E501

urlpatterns = [
    path("", SkillListAPIView.as_view(), name="skill"),
    path("<slug>", UserSkillListAPIView.as_view(), name="user_skill_get"),
    path("user/", UserSkillAPIView.as_view(), name="user_skill_post"),
    path("<int:pk>/", UserSkillDetailAPIView.as_view(), name="user_skill_update"),
]
