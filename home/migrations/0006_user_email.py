# Generated by Django 3.2.5 on 2021-08-08 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_user_django_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='202120818@hwamyeong.hs.kr', max_length=254),
            preserve_default=False,
        ),
    ]
