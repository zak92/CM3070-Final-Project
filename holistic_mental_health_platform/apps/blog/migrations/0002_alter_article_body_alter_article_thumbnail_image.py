# Generated by Django 4.0.4 on 2022-07-06 17:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='thumbnail_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
