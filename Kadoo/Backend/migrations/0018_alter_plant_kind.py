# Generated by Django 3.2.8 on 2021-11-30 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0017_plant_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='kind',
            field=models.CharField(blank=True, default='Plant', editable=False, max_length=10),
        ),
    ]
