# Generated by Django 5.1.3 on 2024-11-22 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='city',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
