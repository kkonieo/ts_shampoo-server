from .models import Project
# from apps.user.serializers import UserSerializer
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "author_email",
            "title",
            "startDate",
            "endDate",
            "techStack",
            "explain",
            "imgSrc",
            "gifSrc",
        ]
    
    author_email = serializers.SerializerMethodField('get_authors_email')
    
    def get_authors_email(self, obj):
        return obj.author.email
    
class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "author_email",
            "title",
            "startDate",
            "endDate",
            "techStack",
            "explain",
            "imgSrc",
            "gifSrc",
        ]
    
    author_email = serializers.SerializerMethodField('get_authors_email')
    
    def get_authors_email(self, obj):
        return obj.author.email