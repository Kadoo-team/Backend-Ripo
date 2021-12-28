# Generated by Django 3.2.8 on 2021-12-28 08:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Green_House', '0008_auto_20211111_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myplant',
            name='plant',
        ),
        migrations.AddField(
            model_name='myplant',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myplant',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
