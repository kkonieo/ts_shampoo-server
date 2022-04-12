from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from apps.user.models import User
from .models import Skill, UserSkill
from .serializers import SkillSerializer, UserSkillSerializer


class SkillListAPIView(ListAPIView):
    """
    skill 목록 조회

    비회원도 조회 가능
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class UserSkillAPIView(APIView):
    """
    사용자 skill 목록 생성

    access token으로 허가된 사용자 가능
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=UserSkillSerializer,
        responses={
            status.HTTP_201_CREATED: UserSkillSerializer,
            status.HTTP_400_BAD_REQUEST: "잘못된 요청",
            status.HTTP_401_UNAUTHORIZED: "권한 없음",
            status.HTTP_405_METHOD_NOT_ALLOWED: "메서드 매칭되지 않음",
        },
    )
    def post(self, request):
        user = request.user.id
        serializer = UserSkillSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            user_has_skill = UserSkill.objects.filter(user_id=request.user.id).filter(skill_id=request.data["skill"])   # noqa : E501
            if user_has_skill:
                return Response({"detail": "user skill already exist"},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                user_skill = UserSkill()
                user_skill.user_id = user
                user_skill.skill_id = request.data["skill"]
                user_skill.content = validated_data["content"]
                user_skill.save()
                return Response({"detail": "success create user_skill"},
                                status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSkillDetailAPIView(APIView):
    # todo : 다른 user는 수정, 삭제 권한 못하도록
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(UserSkill, pk=pk)

    @swagger_auto_schema(
        request_body=UserSkillSerializer,
        responses={
            status.HTTP_200_OK: UserSkillSerializer,
            status.HTTP_401_UNAUTHORIZED: "권한 없음",
            status.HTTP_400_BAD_REQUEST: "잘못된 요청",
            status.HTTP_404_NOT_FOUND: "해당 기술이 존재하지 않음",
        },
    )
    def put(self, request, pk):
        """
        사용자 skill 수정

        access token으로 허가된 사용자 가능
        """
        user_skill = self.get_object(pk)
        serializer = UserSkillSerializer(user_skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "success update"},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "성공",
            status.HTTP_401_UNAUTHORIZED: "권한 없음",
            status.HTTP_404_NOT_FOUND: "해당 기술이 존재하지 않음",
            status.HTTP_405_METHOD_NOT_ALLOWED: "메서드 매칭되지 않음",
        },
    )
    def delete(self, request, pk):
        """
        사용자 skill 삭제

        access token으로 허가된 사용자 가능
        """
        user_skill = self.get_object(pk)
        user_skill.delete()
        return Response({"detail": "success delete"},
                        status=status.HTTP_200_OK)


class UserSkillListAPIView(ListAPIView):
    """
    사용자 skill 목록 조회

    비회원도 조회 가능
    """
    def get(self, request, *args, **kwargs):
        user = User.objects.get(slug=self.kwargs['slug'])
        queryset = UserSkill.objects.filter(user_id=user.id)
        serializer = UserSkillSerializer(queryset, many=True)
        return Response(serializer.data)
