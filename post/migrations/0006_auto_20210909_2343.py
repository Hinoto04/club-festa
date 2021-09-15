# Generated by Django 3.2.5 on 2021-09-09 14:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20210909_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='notice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.notice'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='hotDate',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 9, 9, 23, 43, 18, 54677)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='publicDate',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 9, 9, 23, 43, 18, 54677)),
        ),
    ]