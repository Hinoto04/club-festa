# Generated by Django 3.2.5 on 2021-11-12 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0009_club_appli'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='appli',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='club',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='club',
            name='member_detail',
            field=models.TextField(default='', null=True),
        ),
    ]
