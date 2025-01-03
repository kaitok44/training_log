from django.urls import path

from .views import (
    ExerciseListView,
    ExerciseDetailView,
    ExerciseUpdateView,
    ExerciseDeleteView,
    ExerciseCreateView,
)

urlpatterns = [
    path("<int:pk>/", ExerciseDetailView.as_view(),
        name="exercise_detail"),
    path("<int:pk>/edit/", ExerciseUpdateView.as_view(),
        name="exercise_edit"),
    path("<int:pk>/delete/", ExerciseDeleteView.as_view(),
        name="exercise_delete"),
    path("new/", ExerciseCreateView.as_view(), name="exercise_new"),
    path("", ExerciseListView.as_view(), name="exercise_list"),
]
