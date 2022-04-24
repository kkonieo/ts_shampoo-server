from rest_framework import serializers

from .models import Skill, UserSkill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class UserSkillBaseSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(read_only=True)

    class Meta:
        model = UserSkill
        fields = ("skill",)


class UserSkillSerializer(UserSkillBaseSerializer, serializers.ModelSerializer):

    class Meta:
        model = UserSkill
        fields = ("content",)


class UserSkillListSerializer(serializers.ModelSerializer):
    skill = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = UserSkill
        fields = ("skill",
                  "description",)

    def get_skill(self, obj):
        skill = Skill.objects.values("id", "name").get(id=obj["skill_id"])
        return skill

    def get_description(self, obj):
        queryset = UserSkill.objects.values("id", "content").filter(skill_id=obj["skill_id"]) # noqa : E501
        return queryset
