# Generated by Django 5.0.10 on 2025-01-12 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("workout", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="workoutsession",
            old_name="workout_session_name",
            new_name="name",
        ),
    ]
