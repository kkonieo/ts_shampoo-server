from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin,)
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from apps.core.helper import generate_nanoid


# user를 생성할 때 사용하는 helper class
class UserManager(BaseUserManager):
    def create_user(self, name, email, img, password=None):

        if email is None:
            raise TypeError("Users should have a Email")

        if name is None:
            raise TypeError("Users should have a username")

        user = self.model(
            name=name,
            email=self.normalize_email(email),
            img=img,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, name, email, password=None):
        if password is None:
            raise TypeError("Password should not be none")

        user = self.create_user(
            name,
            email,
            password,
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


# 실제 모델을 생성하는 class
class User(AbstractBaseUser, PermissionsMixin):
    """
    사용자 정의모델
    AUTH_PROVIDERS = 소셜 구분
    name : 이름

    """

    AUTH_PROVIDERS = {
        "naver": "naver",
        "google": "google",
        "github": "github",
        "email": "email",
    }
    # 소셜 구분

    name = models.CharField(verbose_name="유저 이름", max_length=10, db_index=True)
    email = models.EmailField(
        verbose_name="email", max_length=255, unique=True, db_index=True
    )
    slug = models.SlugField(
        verbose_name=("slug"),
        unique=True,
        default=generate_nanoid,
        max_length=40,
    )
    job = models.CharField(verbose_name="직군", max_length=100)
    img = models.CharField(verbose_name="이미지", max_length=200, null=True, blank=True)
    github = models.CharField(verbose_name="깃헙 주소", max_length=200, null=True, blank=True)  # noqa : E501
    is_active = models.BooleanField(verbose_name="기본 권한", default=True)
    is_staff = models.BooleanField(verbose_name="슈퍼 유저", default=False)
    is_verified = models.BooleanField(verbose_name="email 인증자", default=False)
    auth_provider = auth_provider = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        default=AUTH_PROVIDERS.get("email"),
    )
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email

    # 로그인한 사용자에게 refresh 토큰을 생성해서 부여한다.
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        access = refresh.access_token
        return {
            "refresh": str(refresh),
            "access": str(access),
            "expired": str(access["exp"]),
        }
