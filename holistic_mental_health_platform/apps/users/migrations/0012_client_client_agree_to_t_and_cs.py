# Generated by Django 4.0.4 on 2022-04-30 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_client_client_agree_to_t_and_cs'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_agree_to_T_and_Cs',
            field=models.BooleanField(default=False),
        ),
    ]
