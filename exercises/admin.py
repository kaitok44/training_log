from django.contrib import admin
from .models import Exercise

class ExerciseAdmin(admin.ModelAdmin):
    list_display = [
        "exercise_name",
        "muscles_worked",
        "notes",
        "author",
    ]

admin.site.register(Exercise, ExerciseAdmin)
# Register your models here.
