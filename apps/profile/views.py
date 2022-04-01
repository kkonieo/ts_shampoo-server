from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.user.models import User
from .models import Profile
from .serializers import ProfileSerializer


class ProfileAPIView(APIView):
    """
    about me 생성, 수정, 삭제
    access token으로 허가된 사용자 가능
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user.id
        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data

            profile = Profile()
            profile.author_id = user
            profile.content = validated_data["content"]
            profile.save()
            return Response({"detail": "success create profile"})

        return Response(serializer.errors)

    # to do : 추가기능_한번만 생성하고 2번이상 생성 불가하도록

    def put(self, request):
        user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(author_id=user.id)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True,
                            "detail": "success update"},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        profile = Profile.objects.filter(author_id=request.user.id)
        profile.delete()
        return Response({"result": "profile delete"})

    # to do : 추가기능_삭제한 후 다시 삭제하려하면 안된다는 메세지 띄우도록


class ProfileRetrieveAPIView(APIView):
    """
    slug로 about me 조회
    누구나
    """
    def get(self, request, *args, **kwargs):
        user = User.objects.get(slug=self.kwargs['slug'])
        queryset = Profile.objects.filter(author_id=user.id)
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)
