# Generated by Django 5.1.3 on 2024-11-10 02:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_console', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productID', models.CharField(editable=False, max_length=30, primary_key=True, serialize=False)),
                ('productname', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('category', models.CharField(choices=[('Electronics', 'Electronics'), ('Kitchen Appliances', 'Kitchen Appliances'), ('Home Appliances', 'Home Appliances'), ('Entertainment', 'Entertainment'), ('Books', 'Books')], max_length=20)),
                ('imageUrl', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='product_mgmt.product')),
                ('rated_by', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_console.user')),
            ],
        ),
    ]
