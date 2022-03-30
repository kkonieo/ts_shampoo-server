# Generated by Django 4.0.2 on 2022-03-30 04:22

import apps.core.helper
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(db_index=True, max_length=10, verbose_name='유저 이름')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='email')),
                ('slug', models.SlugField(default=apps.core.helper.generate_nanoid, max_length=40, unique=True, verbose_name='slug')),
                ('job', models.CharField(max_length=100, verbose_name='직군')),
                ('img', models.CharField(blank=True, max_length=200, null=True, verbose_name='이미지')),
                ('github', models.CharField(blank=True, max_length=200, null=True, verbose_name='깃헙 주소')),
                ('is_active', models.BooleanField(default=True, verbose_name='기본 권한')),
                ('is_staff', models.BooleanField(default=False, verbose_name='슈퍼 유저')),
                ('is_verified', models.BooleanField(default=False, verbose_name='email 인증자')),
                ('auth_provider', models.CharField(default='email', max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
