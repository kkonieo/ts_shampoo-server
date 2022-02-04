# Generated by Django 4.0.1 on 2022-02-03 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('startDate', models.DateField(verbose_name='시작일')),
                ('endDate', models.DateField(verbose_name='종료일')),
                ('techStack', models.TextField(verbose_name='기술스택')),
                ('explain', models.TextField(verbose_name='내용')),
                ('imgSrc', models.ImageField(blank=True, null=True, upload_to='projectImg/', verbose_name='png이미지소스')),
                ('gifSrc', models.ImageField(blank=True, null=True, upload_to='projectImg/', verbose_name='gif이미지소스')),
                ('demoUrlLink', models.URLField(null=True, verbose_name='demoUrl')),
                ('gitUrlLink', models.URLField(null=True, verbose_name='gitUrl')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
