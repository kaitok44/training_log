# Generated by Django 5.0.10 on 2025-01-03 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exercises", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exercise",
            name="notes",
            field=models.TextField(blank=True),
        ),
    ]
