from rest_framework import serializers

from .models import Award, Profile, Resume, Skill, UserSkill

# class ProfileSerializer(serializers.HyperlinkedModelSerializer):
#         url = serializers.HyperlinkedIdentityField(
#         view_name= 'profile_detail',
#         lookup_field = 'author_id'
#     )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class UserSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSkill
        fields = '__all__'
