# Generated by Django 3.2.5 on 2021-08-03 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='user',
            name='room',
        ),
    ]
