# from apps.user.serializers import UserSerializer
from rest_framework import serializers

from .models import Project, ProjectLink


class ProjectLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectLink
        fields = [
            "linkName",
            "linkUrl",
        ]


class ProjectSerializer(serializers.ModelSerializer):
    # urlLink = ProjectLinkSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "author_id",
            "title",
            "startDate",
            "endDate",
            "techStack",
            "explain",
            "imgSrc",
            "gifSrc",
        ]


class ProjectDetailSerializer(serializers.ModelSerializer):
    # urlLink = ProjectLinkSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "author_id",
            "title",
            "startDate",
            "endDate",
            "techStack",
            "explain",
            "imgSrc",
            "gifSrc",
        ]
