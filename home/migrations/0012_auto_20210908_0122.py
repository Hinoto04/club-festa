# Generated by Django 3.2.5 on 2021-09-07 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210908_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='noticelike',
            field=models.TextField(default='/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='like',
            field=models.TextField(default='/'),
        ),
    ]
