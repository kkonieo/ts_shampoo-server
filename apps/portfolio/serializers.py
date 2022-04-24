# from apps.user.serializers import UserSerializer
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from .models import Project, ProjectLink


class ProjectLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectLink
        fields = '__all__'


class ProjectSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    urlLink = ProjectLinkSerializer(many=True, source='projectLink')

    class Meta:
        model = Project
        fields = '__all__'
        depth = 1


class ProjectDetailSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):  # noqa : W503
    urlLink = ProjectLinkSerializer(many=True, source='projectLink')

    class Meta:
        model = Project
        fields = '__all__'
