# Generated by Django 3.2.5 on 2021-09-11 12:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20210909_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='like',
        ),
        migrations.AlterField(
            model_name='notice',
            name='hotDate',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 9, 11, 21, 50, 34, 813700)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='publicDate',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 9, 11, 21, 50, 34, 813700)),
        ),
    ]
