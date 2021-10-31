# Generated by Django 3.2.5 on 2021-10-31 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0014_remove_user_isactive'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLoginLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP Address')),
                ('user_agent', models.CharField(max_length=300, verbose_name='HTTP User Agent')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='login_logs', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'user login log',
                'verbose_name_plural': 'user login logs',
                'ordering': ('-created',),
            },
        ),
    ]