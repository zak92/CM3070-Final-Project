# Generated by Django 4.0.4 on 2022-04-30 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_client_user_alter_serviceprovider_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceprovider',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='serviceprovider',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='roles',
        ),
        migrations.AddField(
            model_name='user',
            name='is_client',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_service_provider',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
