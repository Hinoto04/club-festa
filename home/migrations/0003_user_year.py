# Generated by Django 3.2.5 on 2021-08-03 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210803_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='year',
            field=models.IntegerField(default='2021'),
        ),
    ]
