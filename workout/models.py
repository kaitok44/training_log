from django.db import models
from django.conf import settings
from exercises.models import Exercise
from django.urls import reverse
    
class WorkoutSession(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return f"{self.name} {self.date}"
    
    def get_absolute_url(self):
        return reverse("workout_session_detail", kwargs={'session_pk': self.pk})

class Workout(models.Model):
    workout_session = models.ForeignKey(
        WorkoutSession, on_delete=models.CASCADE,
    )
    exercise = models.ForeignKey(
        Exercise, on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse("workout_session_detail", kwargs={"session_pk": self.workout_session.pk})
    
    def __str__(self):
        return f"{self.workout_session}, {self.exercise}"
    
class Set(models.Model):
    exercise = models.ForeignKey(Workout, on_delete=models.CASCADE)
    set_number = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ('set_number',)

    def __str__(self):
        return f"{self.exercise}, set #{self.set_number}"
    
    # redirect to Workout.pk
    def get_absolute_url(self):
        return reverse("workout_session_detail", kwargs={"session_pk": self.exercise.workout_session.pk})
# Create your models here.