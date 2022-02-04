from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Award, Profile, Resume, Skill, UserSkill
from .serializers import (AwardSerializer, ProfileSerializer, ResumeSerializer,
                          SkillSerializer, UserSkillSerializer,)


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', ]


profile_list = ProfileViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
profile_detail = ProfileViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})


class ResumeViewSet(ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', ]


resume_list = ResumeViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

resume_detail = ResumeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})


class AwardViewSet(ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', ]


award_list = AwardViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

award_detail = AwardViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})


class UserSkillViewSet(ModelViewSet):
    queryset = UserSkill.objects.all()
    serializer_class = UserSkillSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', ]


user_skill_list = UserSkillViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

user_skill_detail = UserSkillViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})
