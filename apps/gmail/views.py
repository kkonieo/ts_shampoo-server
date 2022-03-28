from django.shortcuts import render
from django.core.mail.message import EmailMessage
from config import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

FROM_EMAIL = settings.base.EMAIL_HOST_USER


class SendEmail(APIView):
    """
    이메일 전송
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        email_send = request.data.get("email_send")
        name_send = request.data.get("name_send")
        content = request.data.get("content")
        name_receive = request.data.get("name_receive")
        email_receive = request.data.get("email_receive")

        subject = "ts-shampoo에서 {}님의 이력 보고 제안 드립니다.".format(name_receive)
        to = [email_receive]
        message = "안녕하세요, \nts-shampoo에서 {0}님이 {1}님의 이력을 보고 연락드립니다. \n{2}로 회신 부탁드립니다.\n\n{3}".format(name_send, name_receive, email_send, content) # noqa : E501
        EmailMessage(subject=subject, body=message, to=to, from_email=FROM_EMAIL).send()
        return Response({"message": "ok"})
