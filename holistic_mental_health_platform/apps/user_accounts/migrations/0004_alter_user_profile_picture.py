# Generated by Django 4.0.4 on 2022-06-29 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0003_remove_serviceprovider_phone_no_user_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='profile_pictures/default-user-avatar-000.png', null=True, upload_to='profile_pictures/'),
        ),
    ]