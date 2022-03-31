from django.shortcuts import render
from django.core.mail.message import EmailMessage
from config import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from apps.user.models import User


FROM_EMAIL = settings.base.EMAIL_HOST_USER


class UserEmail(APIView):
    def get(self, request, *args, **kwargs):
        """
        slug로 대상 email 및 정보 조회
        """
        user = User.objects.get(slug=self.kwargs['slug'])
        email = str(user)
        name = str(user.name)
        github = str(user.github)
        return Response({"email": email,
                         "name": name,
                         "github": github})


class SendEmail(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        이메일 전송
        """
        from_email = request.data.get("from_email")
        from_name = request.data.get("from_name")
        email_text = request.data.get("email_text")
        to_email = request.data.get("to_email")
        to_name = request.data.get("to_name")

        subject = "ts-shampoo에서 {}님의 이력 보고 제안 드립니다.".format(to_name)
        to = [to_email]
        message = "안녕하세요, \nts-shampoo에서 {0}님이 {1}님의 이력을 보고 연락드립니다. \n{2}로 회신 부탁드립니다.\n\n{3}".format(from_name, to_name, from_email, email_text) # noqa : E501
        EmailMessage(subject=subject, body=message, to=to, from_email=FROM_EMAIL).send()
        return Response({"message": "true"})
