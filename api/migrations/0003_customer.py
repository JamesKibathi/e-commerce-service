# Generated by Django 4.2.19 on 2025-02-11 06:52

import api.utils.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_date_joined'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=api.utils.helpers.get_uuid, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=256)),
                ('phonenumber', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address', models.CharField(blank=True, max_length=256)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
