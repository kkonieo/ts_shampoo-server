from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from .models import Skill, UserSkill
from .serializers import SkillSerializer, UserSkillSerializer


class UserSkillViewSet(ModelViewSet):
    queryset = UserSkill.objects.all()
    serializer_class = UserSkillSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "user",
    ]


user_skill_list = UserSkillViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

user_skill_detail = UserSkillViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
    }
)
