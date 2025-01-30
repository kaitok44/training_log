from django.contrib import admin
from .models import Workout, Set, WorkoutSession

class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "author",
        "workout_date",
    ]

class WorkoutAdmin(admin.ModelAdmin):
    list_display = [
        "workout_session",
        "exercise",
    ]

class SetAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "weight",
        "repetitions",
        "notes",
    ]
    
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Set, SetAdmin)
admin.site.register(WorkoutSession, WorkoutSessionAdmin)
# Register your models here.
