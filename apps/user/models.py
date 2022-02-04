from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin,)
from django.db import models


# user를 생성할 때 사용하는 helper class
class UserManager(BaseUserManager):
    def create_user(self, name, email, password=None):

        if email is None:
            raise TypeError("Users should have a Email")

        if name is None:
            raise TypeError("Users should have a username")

        user = self.model(
            name=name,
            email=self.normalize_email(email),
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
    """

    name = models.CharField(verbose_name="유저 이름", max_length=10, db_index=True)
    email = models.EmailField(
        verbose_name="email", max_length=255, unique=True, db_index=True
    )
    job = models.CharField(verbose_name="직군", max_length=100)
    img = models.CharField(verbose_name="이미지", max_length=200, null=True, blank=True)
    is_active = models.BooleanField(verbose_name="기본 권한", default=True)
    is_staff = models.BooleanField(verbose_name="슈퍼 유저", default=False)
    is_verified = models.BooleanField(verbose_name="email 인증자", default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email