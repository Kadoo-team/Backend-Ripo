# Generated by Django 3.2.8 on 2021-10-21 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0005_plant_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
