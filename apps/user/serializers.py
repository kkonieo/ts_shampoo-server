import os

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from . import google
from .models import User
from .register import register_social_user


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data["sub"]  # 사용자 정보를 올바르게 얻음.
        except:  # noqa: E722
            raise serializers.ValidationError(
                "The token is invalid or expired. Please login again."
            )

        if user_data["aud"] != os.environ.get("SOCIAL_AUTH_GOOGLE_CLIENT_ID"):
            # 구글 클라이언트 ID가 올바르지 않다면

            raise AuthenticationFailed("oops, who are you?")

        email = user_data["email"]
        name = user_data["name"]
        provider = "google"
        img = user_data["picture"]

        return register_social_user(
            provider=provider,
            email=email,
            name=name,
            img=img,
        )


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        "bad_token": {"Token is expired or Invalid"},
    }

    def validate(self, attrs):
        self.token = attrs["refresh"]

        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
            # 토큰을 블랙리스트에 추가.
        except TokenError:
            self.fail("bad token")


class UserUpdateSerializer(serializers.Serializer):
    """
    user 정보 변경
    """

    # 새로 설정될 token

    job = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=10)
    email = serializers.EmailField(max_length=255)

    # uidb64 = serializers.CharField(
    #     min_length=1,
    #     write_only=True,
    # )

    class Meta:
        fields = ["job", "name", "email"]

    def validate(self, attrs):
        try:
            job = attrs.get("job")
            name = attrs.get("name")
            # 새로운 패스워드
            # uidb64 = attrs.get("uidb64")
            # 사용자 index 인코딩 정보 => 이메일로 인증 하는 것이 아닌 uidb로 인증.

            email = attrs.get("email")

            # id = force_str(urlsafe_base64_decode(uidb64))
            # 사용자 index 디코딩 정보
            user = User.objects.get(email=email)
            # 사용자 index 디코딩 정보를 바탕으로한 사용자 정보

            user.job = job
            user.name = name
            # 정보 재설정

            user.save()
            # 변경 정보 저장
        except Exception:
            raise AuthenticationFailed("The reset link is invalid", 401)

        return super().validate(attrs)
