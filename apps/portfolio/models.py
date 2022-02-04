from django.db import models

# Create your models here.

from django.db import models
from django.forms import URLField
from apps.user.models import User


class Project(models.Model):
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField("제목", max_length=50, null=False)
    startDate = models.DateField("시작일", null=False)
    endDate = models.DateField("종료일", null=False)
    techStack = models.TextField("기술스택", null=False)
    explain = models.TextField("내용", null=False)
    imgSrc = models.ImageField("png이미지소스", upload_to='projectImg/', blank=True, null=True)
    gifSrc = models.ImageField("gif이미지소스", upload_to='projectImg/', blank=True, null=True)
    
    demoUrlLink = models.URLField("demoUrl", null=True)
    gitUrlLink = models.URLField("gitUrl", null=True)

    def __str__(self):
        return self.title
