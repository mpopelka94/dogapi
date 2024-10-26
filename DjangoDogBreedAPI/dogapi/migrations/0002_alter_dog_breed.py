# Generated by Django 5.1.1 on 2024-10-25 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dogs', to='dogapi.breed'),
        ),
    ]