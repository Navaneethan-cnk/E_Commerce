# Generated by Django 5.1.3 on 2024-11-26 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_console', '0001_initial'),
        ('product_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='admin_console.user'),
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('rated_by', 'product'), name='unique_review_per_product'),
        ),
    ]