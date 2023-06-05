# Generated by Django 4.1.7 on 2023-04-07 04:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('count', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('album', models.JSONField(blank=True, null=True)),
                ('tags', models.ManyToManyField(to='common.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('count', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('album', models.JSONField(blank=True, null=True)),
                ('environment', models.IntegerField(blank=True, choices=[(0, 'tropical'), (1, 'cold'), (2, 'none')], null=True)),
                ('water', models.IntegerField(blank=True, choices=[(0, 'low'), (1, 'medium'), (2, 'much')], null=True)),
                ('light', models.IntegerField(blank=True, choices=[(0, 'low'), (1, 'medium'), (2, 'much')], null=True)),
                ('growth_rate', models.IntegerField(blank=True, choices=[(0, 'low'), (1, 'medium'), (2, 'much')], null=True)),
                ('tags', models.ManyToManyField(to='common.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
