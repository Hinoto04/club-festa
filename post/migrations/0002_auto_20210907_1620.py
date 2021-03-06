# Generated by Django 3.2.7 on 2021-09-07 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='notice',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='notice',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
