import os
import random

from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

from .models import User


def generate_name(name):
    '''
        이름 생성.
    '''
    name = "".join(name.split(" ")).lower()
    if not User.objects.filter(name=name).exists():
        return name
    else:
        random_name = name + str(random.randint(0, 1000))
        return generate_name(random_name)


def register_social_user(provider, user_id, email, name):
    filtered_user_by_email = User.objects.filter(email=email)
    # user가 이미 있는지 확인
    register_check = False
    # 사용자 회원가입 여부
    if filtered_user_by_email.exists():

        if provider == filtered_user_by_email[0].auth_provider:
            registered_user = authenticate(
                email=email, password=os.environ.get("SOCIAL_SECRET")
            )
            # 유저가 존재하는 경우. email과 password를 통해 자격 검증을 수행한다.
            register_check = True
            # 가입이 되어있는지 체크
            return {
                "user_id": user_id,
                "name": registered_user.name,
                "email": registered_user.email,
                "tokens": registered_user.tokens(),
                "register_check": str(register_check)
            }
            # 자격 검증을 통과하는 경우 유저의 이름과 email tokens를 반환한다.

        else:
            raise AuthenticationFailed(
                detail="Please continue your login using "
                + filtered_user_by_email[0].auth_provider  # noqa:W503
            )

    else:
        user = {
            "name": generate_name(name),
            "email": email,
            "password": os.environ.get("SOCIAL_SECRET"),
        }
        user = User.objects.create_user(**user)
        user.is_verified = True
        # Social 로그인 시 구글과 같은 기업들을 신뢰하기 때문에 email 인증을 True로 반환한다.
        user.auth_provider = provider
        user.save()

        new_user = authenticate(email=email, password=os.environ.get("SOCIAL_SECRET"))
        # 마찬가지로 자격검증을 수행한다.
        return {
            "user_id": user_id,
            "email": new_user.email,
            "name": new_user.name,
            "tokens": new_user.tokens(),
            "register_check": str(register_check)
        }
