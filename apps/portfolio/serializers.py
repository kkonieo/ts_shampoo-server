from .models import Project
# from apps.user.serializers import UserSerializer
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
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
            "demoUrlLink",
            "gitUrlLink",
        ]
    
class ProjectDetailSerializer(serializers.ModelSerializer):
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
            "demoUrlLink",
            "gitUrlLink",
        ]