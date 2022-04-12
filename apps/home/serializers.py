from ..user.models import User

from rest_framework import serializers
from ..skill.serializers import UserHasSkillSerializer


class HomeSerializer(serializers.ModelSerializer):
    """메인 페이지 모든 사용자 정보"""

    user_skill = UserHasSkillSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = (
            "id",
            "slug",
            "name",
            "job",
            "user_skill",
            "img",
        )
