# Generated by Django 4.0.4 on 2022-06-29 12:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0007_alter_user_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceprovider',
            name='announcements',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
