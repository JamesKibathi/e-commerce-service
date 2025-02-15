# Generated by Django 4.2.19 on 2025-02-15 17:31

import api.utils.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(default=api.utils.helpers.generate_order_number, max_length=20),
        ),
    ]
