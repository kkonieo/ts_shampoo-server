from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from apps.user.models import User
from .models import Profile
from .serializers import ProfileSerializer


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=ProfileSerializer,
        responses={
            status.HTTP_201_CREATED: ProfileSerializer,
            status.HTTP_401_UNAUTHORIZED: "권한 없음",
            status.HTTP_400_BAD_REQUEST: "잘못된 요청",
        },
    )
    def post(self, request):
        """
        about me 생성

        access token으로 허가된 사용자 가능
        """
        user = request.user.id
        serializer = ProfileSerializer(data=request.data)

        if Profile.objects.filter(author_id=user):
            return Response({"detail": "profile already exist"})

        elif serializer.is_valid():
            validated_data = serializer.validated_data

            profile = Profile()
            profile.author_id = user
            profile.content = validated_data["content"]
            profile.save()
            return Response({"detail": "success create profile"})

        return Response(serializer.errors)

    @swagger_auto_schema(
        request_body=ProfileSerializer,
        responses={
            status.HTTP_200_OK: ProfileSerializer,
            status.HTTP_401_UNAUTHORIZED: "권한 없음",
            status.HTTP_400_BAD_REQUEST: "잘못된 요청",
            status.HTTP_404_NOT_FOUND: "해당 소개가 존재하지 않음",
        },
    )
    def put(self, request):
        """
        about me 수정

        access token으로 허가된 사용자 가능
        """
        user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(author_id=user.id)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "success update"},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "성공",
            status.HTTP_401_UNAUTHORIZED: "권한 없음",
            status.HTTP_404_NOT_FOUND: "해당 소개가 존재하지 않음",
            status.HTTP_405_METHOD_NOT_ALLOWED: "메서드 매칭되지 않음",
        },
    )
    def delete(self, request):
        """
        about me 삭제

        access token으로 허가된 사용자 가능
        """
        profile = Profile.objects.filter(author_id=request.user.id)
        if profile:
            profile.delete()
            return Response({"detail": "sucess delete"},
                            status=status.HTTP_200_OK)
        else:
            return Response({"detail": "profile not exist"},
                            status=status.HTTP_404_NOT_FOUND)


class ProfileRetrieveAPIView(APIView):
    """
    about me 조회

    비회원도 조회 가능
    """
    def get(self, request, *args, **kwargs):
        user = User.objects.get(slug=self.kwargs['slug'])
        queryset = Profile.objects.filter(author_id=user.id)
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data[0])
