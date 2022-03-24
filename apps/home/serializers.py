from ..user.models import User

from rest_framework import serializers


class HomeSerializer(serializers.ModelSerializer):
    """메인 페이지 모든 사용자 정보"""

    user_skill = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "job",
            "user_skill",
            "img",
        )