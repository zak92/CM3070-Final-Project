# Generated by Django 4.0.4 on 2022-05-28 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_booking_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['date']},
        ),
    ]
