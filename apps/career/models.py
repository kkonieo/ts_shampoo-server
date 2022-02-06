from django.conf import settings
from django.db import models

from apps.core.models import TimeStampModel


class Career(TimeStampModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="작성자",
        related_name="career_author",
        on_delete=models.CASCADE,
    )  # noqa : E501
    title = models.CharField(max_length=100, verbose_name="이력제목")
    year = models.IntegerField(verbose_name="연도")
    content = models.TextField(verbose_name="이력내용")
    start_date = models.DateField(verbose_name="시작일")
    end_date = models.DateField(verbose_name="종료일")

    class Meta:
        db_table = "career"

    def __str__(self):
        return self.title
