# Generated by Django 3.2.5 on 2021-09-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20210908_0053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='isHot',
        ),
        migrations.AddField(
            model_name='notice',
            name='hotDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
