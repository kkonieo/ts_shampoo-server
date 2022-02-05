from django.conf import settings
from django.db import models

from apps.core.models import TimeStampModel


class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="기술이름")

    class Meta:
        db_table = "skill"


class UserSkill(models.Model):
    skill = models.ForeignKey(
        "Skill",
        related_name="skill_id",
        verbose_name="기술id",
        on_delete=models.CASCADE,
        db_column="skill_id",
    )  # noqa : E501
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="user_skill",
        verbose_name="작성자",
        on_delete=models.CASCADE,
    )  # noqa : E501
    content = models.TextField(verbose_name="기술설명")

    class Meta:
        db_table = "user_skill"

    def __str__(self):
        return self.UserSkill
