# Generated by Django 4.0.4 on 2022-06-26 09:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('group_sessions', '0004_remove_groupbooking_client_groupbooking_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupbooking',
            name='client',
            field=models.ManyToManyField(null=True, related_name='client_group_sessions', to=settings.AUTH_USER_MODEL),
        ),
    ]