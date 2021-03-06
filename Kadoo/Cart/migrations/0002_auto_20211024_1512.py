# Generated by Django 3.2.8 on 2021-10-24 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantcartmodel',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='toolcartmodel',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(blank=True, choices=[('approved', 'approved'), ('preparing', 'preparing'), ('ready to deliver', 'ready to deliver'), ('delivering', 'delivering'), ('complete', 'complete')], default='approved', max_length=50, null=True)),
                ('total_price', models.IntegerField(blank=True, default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_delivered', models.BooleanField(default=False)),
                ('order_plants', models.ManyToManyField(blank=True, to='Cart.PlantCartModel')),
                ('order_tools', models.ManyToManyField(blank=True, to='Cart.ToolCartModel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
