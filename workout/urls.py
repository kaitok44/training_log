from .views import (
    WorkoutSessionListView,
    WorkoutSessionDetailView,
    WorkoutSetUpdateView,
    WorkoutSetDeleteView,
    WorkoutSetCreateView,
)
from django.urls import path

urlpatterns = [
    path("", WorkoutSessionListView.as_view(), name="workout_session_list"),
    path("<int:session_pk>/", WorkoutSessionDetailView.as_view(),
        name="workout_session_detail"),
    path("<int:workout_pk>/set/<int:set_pk>/edit/", WorkoutSetUpdateView.as_view(),
        name="workout_set_edit"),
    path("<int:workout_pk>/set/<int:set_pk>/delete/", WorkoutSetDeleteView.as_view(),
        name="workout_set_delete"),
    path("<int:workout_pk>/set/new/", WorkoutSetCreateView.as_view(), name="workout_set_new"),
]

