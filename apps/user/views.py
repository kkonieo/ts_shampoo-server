from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.permissions import IsAuthenticated

from .serializers import (GoogleSocialAuthSerializer, LogoutSerializer,
                          UserUpdateSerializer,)


class GoogleSocialAuthView(GenericAPIView):
    '''
        계정 등록 + 로그인
    '''
    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        """
        id 토큰을 받아서 구글로부터 유저 정보를 생성하거나 확인한다.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = (serializer.validated_data)["auth_token"]
        return Response(data, status=status.HTTP_200_OK)


class LogoutAPIView(GenericAPIView):
    serializer_class = LogoutSerializer

    permison_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(GenericAPIView):
    serializer_class = UserUpdateSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        return Response(
            {
                "success": True,
                "message": "Patch success",
            },
            status=status.HTTP_200_OK,
        )


class UserTokenRefreshView(TokenRefreshView):

    def post(self, request, *args, **kwargs):
        """
        토큰 갱신
        refresh 토큰을 전송하고 새로운 access 토큰값을 발급받습니다.
        """
        return super().post(request, *args, **kwargs)


class DeleteUserView(APIView):
    """
    탈퇴시 계정 삭제
    """
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        user.delete()

        return Response({"result": "user delete"})
