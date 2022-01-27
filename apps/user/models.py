from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# user를 생성할 때 사용하는 helper class
class UserManager(BaseUserManager):
    def create_user(self, name, email, job, img, password=None):
        if not name:
            raise ValueError('must have user name')
        if not email:
            raise ValueError('must have user email')
        user = self.model(
            name=name,
            email=self.normalize_email(email),
            job=job,
            img=img
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, job, img=None, password=None):
            user = self.create_user(
                name=name,
                email=self.normalize_email(email),
                job=job,
                img=img,
                password=password
            )
            user.is_admin = True
            user.save(using=self._db)
            return user

# 실제 모델을 생성하는 class
class User(AbstractBaseUser):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=100,unique=True, primary_key=True)
    job = models.CharField(max_length=100)
    img = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','job']
    
    def __str__(self):
        return self.name

    # 뷰 함수 내부에서 사용자가 특정 권한 갖고 있는지 확인
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # @는 권한을 뷰 함수 전체에 적용해야하는 경우
    @property
    def is_staff(self):
        return self.is_admin