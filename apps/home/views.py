from django.shortcuts import render

from rest_framework.generics import ListAPIView

from ..user.models import User
from .serializers import HomeSerializer


class HomeListAPIView(ListAPIView):
    """
    메인 페이지 모든 사용자 정보 조회
    """

    queryset = User.objects.exclude(job='').order_by("-updated_at")
    serializer_class = HomeSerializer
