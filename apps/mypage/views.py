from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from .models import Profile, Resume, Award, Skill, UserSkill
from .serializers import ProfileSerializer, ResumeSerializer, AwardSerializer, SkillSerializer, UserSkillSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

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

award_list = AwardViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

award_detail = AwardViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

# class SkillViewSet(ModelViewSet):
#     queryset = Skill.objects.all()
#     serializer_class = SkillSerializer

class UserSkillViewSet(ModelViewSet):
    queryset = UserSkill.objects.all()
    serializer_class = UserSkillSerializer

user_skill_list = UserSkillViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

user_skill_detail = UserSkillViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})
