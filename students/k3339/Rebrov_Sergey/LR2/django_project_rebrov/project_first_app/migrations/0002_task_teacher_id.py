# Generated by Django 5.1.2 on 2024-11-10 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='teacher_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='project_first_app.schooluser'),
            preserve_default=False,
        ),
    ]
