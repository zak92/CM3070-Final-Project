# Generated by Django 4.0.4 on 2022-05-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_alter_booking_service_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
