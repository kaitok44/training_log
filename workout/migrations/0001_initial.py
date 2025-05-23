# Generated by Django 5.0.10 on 2025-01-12 11:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("exercises", "0004_delete_workout"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Workout",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "exercise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exercises.exercise",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Set",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("set_number", models.PositiveIntegerField()),
                ("repetitions", models.PositiveIntegerField()),
                ("weight", models.DecimalField(decimal_places=2, max_digits=5)),
                ("notes", models.TextField(blank=True)),
                (
                    "exercise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="workout.workout",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WorkoutSession",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("workout_session_name", models.CharField(max_length=255)),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="workout",
            name="workout_session",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="workout.workoutsession"
            ),
        ),
    ]
