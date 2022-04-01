from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from apps.user.models import User
from .models import Award
from .serializers import AwardSerializer


class AwardAPIView(APIView):
    """
    award 생성

    access token으로 허가된 사용자 가능
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=AwardSerializer,
        responses={
            status.HTTP_201_CREATED: AwardSerializer,
            status.HTTP_401_UNAUTHORIZED: "권한 없음",
            status.HTTP_400_BAD_REQUEST: "잘못된 요청",
        },
    )
    def post(self, request):
        user = request.user.id
        serializer = AwardSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data

            award = Award()
            award.author_id = user
            award.award = validated_data["award"]
            award.year = validated_data["year"]
            award.content = validated_data["content"]
            award.save()
            return Response({"detail": "success create award"})

        return Response(serializer.errors)


class AwardDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Award, pk=pk)

    @swagger_auto_schema(
        request_body=AwardSerializer,
        responses={
            status.HTTP_200_OK: AwardSerializer,
            status.HTTP_401_UNAUTHORIZED: "권한 없음",
            status.HTTP_400_BAD_REQUEST: "잘못된 요청",
            status.HTTP_404_NOT_FOUND: "해당 수상 이력이 존재하지 않음",
            status.HTTP_405_METHOD_NOT_ALLOWED: "메서드 매칭되지 않음",
        },
    )
    def put(self, request, pk):
        """
        award 수정

        access token으로 허가된 사용자 가능
        """
        award = self.get_object(pk)
        serializer = AwardSerializer(award, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "success update"},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "성공",
            status.HTTP_401_UNAUTHORIZED: "권한 없음",
            status.HTTP_404_NOT_FOUND: "해당 수상 이력이 존재하지 않음",
        },
    )
    def delete(self, request, pk):
        """
        award 삭제

        access token으로 허가된 사용자 가능
        """
        award = self.get_object(pk)
        award.delete()
        return Response({"detail": "success delete"},
                        status=status.HTTP_200_OK)


class AwardListAPIView(ListAPIView):
    """
    award list 조회

    비회원도 조회 가능
    """
    def get(self, request, *args, **kwargs):
        user = User.objects.get(slug=self.kwargs['slug'])
        queryset = Award.objects.filter(author_id=user.id)
        serializer = AwardSerializer(queryset, many=True)
        return Response(serializer.data)
