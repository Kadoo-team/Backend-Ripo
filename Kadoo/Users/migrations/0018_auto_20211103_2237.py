# Generated by Django 3.2.8 on 2021-11-03 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0017_alter_specilistfields_degree'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specilistfields',
            name='user',
        ),
        migrations.DeleteModel(
            name='Specialist',
        ),
        migrations.DeleteModel(
            name='SpecilistFields',
        ),
    ]
