from google.auth.transport import requests
from google.oauth2 import id_token


class Google:
    """
        구글 유저 정보를 반환.
    """

    @staticmethod
    def validate(auth_token):
        """
            사용자 정보를 가져오기 위해서 Google OAUTH 2 API를 확인한다.
        """
        try:
            idinfo = id_token.verify_oauth2_token(
                auth_token,
                requests.Request(),
            )
            # 가져온 auth_token이 맞는지 검증한다.

            if "accounts.google.com" in idinfo["iss"]:
                return idinfo

        except:  # noqa:E722
            return "The token is either invalid or has expired"
