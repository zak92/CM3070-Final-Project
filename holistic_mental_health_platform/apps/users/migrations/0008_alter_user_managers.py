# Generated by Django 4.0.4 on 2022-04-30 15:28

import apps.users.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_serviceprovider_about_alter_client_bio'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', apps.users.models.CustomUserManager()),
            ],
        ),
    ]