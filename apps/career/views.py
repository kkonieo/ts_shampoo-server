from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from apps.user.models import User
from .models import Career
from .serializers import CareerSerializer


class CareerAPIView(APIView):
    """
    career 생성

    access token으로 허가된 사용자 가능
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=CareerSerializer,
        responses={
            status.HTTP_201_CREATED: CareerSerializer,
            status.HTTP_401_UNAUTHORIZED: "권한 없음",
            status.HTTP_400_BAD_REQUEST: "잘못된 요청",
        },
    )
    def post(self, request):
        user = request.user.id
        serializer = CareerSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data

            career = Career()
            career.author_id = user
            career.title = validated_data["title"]
            career.year = validated_data["year"]
            career.start_date = validated_data["start_date"]
            career.end_date = validated_data["end_date"]
            career.content = validated_data["content"]
            career.save()
            return Response({"detail": "success create career"})

        return Response(serializer.errors)

    # to do : 추가기능_한번만 생성하고 2번이상 생성 불가하도록


class CareerDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Career, pk=pk)

    @swagger_auto_schema(
        request_body=CareerSerializer,
        responses={
            status.HTTP_200_OK: CareerSerializer,
            status.HTTP_401_UNAUTHORIZED: "권한 없음",
            status.HTTP_400_BAD_REQUEST: "잘못된 요청",
            status.HTTP_404_NOT_FOUND: "해당 경력이 존재하지 않음",
        },
    )
    def put(self, request, pk):
        """
        career 수정

        access token으로 허가된 사용자 가능
        """
        career = self.get_object(pk)
        serializer = CareerSerializer(career, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "success update"},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "성공",
            status.HTTP_401_UNAUTHORIZED: "권한 없음",
            status.HTTP_404_NOT_FOUND: "해당 경력이 존재하지 않음",
        },
    )
    def delete(self, request, pk):
        """
        career 삭제

        access token으로 허가된 사용자 가능
        """
        career = self.get_object(pk)
        career.delete()
        return Response({"detail": "success delete"},
                        status=status.HTTP_200_OK)

    # to do : 추가기능_삭제한 후 다시 삭제하려하면 안된다는 메세지 띄우도록


class CareerListAPIView(ListAPIView):
    """
    career list 조회

    비회원도 조회 가능
    """
    def get(self, request, *args, **kwargs):
        user = User.objects.get(slug=self.kwargs['slug'])
        queryset = Career.objects.filter(author_id=user.id)
        serializer = CareerSerializer(queryset, many=True)
        return Response(serializer.data)
