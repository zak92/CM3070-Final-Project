# Generated by Django 4.0.4 on 2022-06-26 11:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('group_sessions', '0006_alter_groupbooking_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupbooking',
            name='client',
        ),
        migrations.RemoveField(
            model_name='groupbooking',
            name='current_members',
        ),
        migrations.AddField(
            model_name='groupbooking',
            name='members',
            field=models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL),
        ),
    ]
