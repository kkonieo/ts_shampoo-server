from django.conf import settings
from django.db import models

from apps.core.models import TimeStampModel


class Award(TimeStampModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="작성자",
        related_name="award_author",
        on_delete=models.CASCADE,
    )  # noqa : E501
    award = models.CharField(max_length=100, verbose_name="수상이름")
    year = models.IntegerField(verbose_name="연도")
    content = models.TextField(verbose_name="수상내용")

    class Meta:
        db_table = "award"

    def __str__(self):
        return self.award
