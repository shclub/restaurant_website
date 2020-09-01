# Generated by Django 3.1 on 2020-08-29 14:51

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=50, verbose_name='닉네임')),
                ('intro', models.TextField(blank=True, max_length=500, verbose_name='소개')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='전화번호')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='사진')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profile',
            },
        ),
    ]
