# Generated by Django 3.2.8 on 2021-11-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Green_House', '0003_auto_20211109_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myplant',
            name='location',
        ),
        migrations.AddField(
            model_name='myplant',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Locations',
        ),
    ]
