# Generated by Django 3.2.5 on 2021-08-14 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_user_lastedit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='user',
            name='interested_in',
            field=models.TextField(default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_message',
            field=models.TextField(default=' ', max_length=200),
        ),
    ]