# Generated by Django 4.0.4 on 2022-08-05 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group_sessions', '0009_alter_groupbooking_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupbooking',
            name='duration',
            field=models.IntegerField(null=True),
        ),
    ]
