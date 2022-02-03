from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

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



