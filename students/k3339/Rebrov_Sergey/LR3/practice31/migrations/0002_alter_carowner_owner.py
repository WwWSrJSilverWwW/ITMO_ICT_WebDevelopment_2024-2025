# Generated by Django 5.1.3 on 2024-11-25 20:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice31', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carowner',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_owner', to='practice31.owner'),
        ),
    ]
