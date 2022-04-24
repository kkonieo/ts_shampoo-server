# Generated by Django 4.0.1 on 2022-02-05 09:30

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
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='기술이름')),
            ],
            options={
                'db_table': 'skill',
            },
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='기술설명')),
                ('skill', models.ForeignKey(db_column='skill_id', on_delete=django.db.models.deletion.CASCADE, related_name='skill_id', to='skill.skill', verbose_name='기술id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_skill', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'db_table': 'user_skill',
            },
        ),
    ]
