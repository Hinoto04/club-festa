# Generated by Django 3.2.5 on 2021-11-12 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0011_auto_20211112_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='appli',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='club',
            name='club_thumbnail',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='club',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='club',
            name='member_detail',
            field=models.TextField(blank=True, default=''),
        ),
    ]