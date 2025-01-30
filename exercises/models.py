from django.db import models
from django.conf import settings
from django.urls import reverse

class Exercise(models.Model):
    MUSCLES_WORKED_CHOICES = (
        ('CH', 'Chest'),
        ('BK', 'Back'),
        ('LG', 'Legs'),
        ('AB', 'Abs'),
        ('SH', 'Shoulders'),
        ('AR', 'Arms'),
    )
    muscles_worked = models.CharField(max_length=2, choices=MUSCLES_WORKED_CHOICES)
    exercise_name = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.exercise_name
    
    def get_absolute_url(self):
        return reverse("exercise_detail", kwargs={"pk": self.pk})
# Create your models here.
