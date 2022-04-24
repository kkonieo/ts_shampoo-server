from django.conf import settings
from django.db import models

from apps.core.models import TimeStampModel


class Profile(TimeStampModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="작성자",
        related_name="profile_author",
        on_delete=models.CASCADE,
    )  # noqa : E501
    content = models.TextField(verbose_name="자기소개")

    class Meta:
        db_table = "profile"

    def __str__(self):
        return self.content
