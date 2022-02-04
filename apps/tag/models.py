from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=100, verbose_name="직군이름")

    class Meta:
        db_table = "job"
