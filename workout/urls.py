from .views import (
    WorkoutSessionListView,
    WorkoutSessionDetailView,
    WorkoutSessionUpdateView,
    WorkoutSessionDeleteView,
    WorkoutSessionCreateView,
    WorkoutCreateView,
    WorkoutUpdateView,
    WorkoutDeleteView,
    WorkoutSetUpdateView,
    WorkoutSetDeleteView,
    WorkoutSetCreateView,
)
from django.urls import path

urlpatterns = [
    path("", WorkoutSessionListView.as_view(), name="workout_session_list"),
    path("<int:session_pk>/", WorkoutSessionDetailView.as_view(),
        name="workout_session_detail"),
    path("<int:session_pk>/edit/", WorkoutSessionUpdateView.as_view(),
        name="workout_session_edit"),
    path("<int:session_pk>/delete/", WorkoutSessionDeleteView.as_view(),
        name="workout_session_delete"),
    path("new/", WorkoutSessionCreateView.as_view(),
        name="workout_session_new"),
    path("<int:session_pk>/new/", WorkoutCreateView.as_view(),
        name="workout_new"),
    path("<int:session_pk>/<int:workout_pk>/edit/", WorkoutUpdateView.as_view(),
        name="workout_edit"),
    path("<int:session_pk>/<int:workout_pk>/delete/", WorkoutDeleteView.as_view(),
        name="workout_delete"),
    path("<int:workout_pk>/set/<int:set_pk>/edit/", WorkoutSetUpdateView.as_view(),
        name="workout_set_edit"),
    path("<int:workout_pk>/set/<int:set_pk>/delete/", WorkoutSetDeleteView.as_view(),
        name="workout_set_delete"),
    path("<int:workout_pk>/set/new/", WorkoutSetCreateView.as_view(),
        name="workout_set_new"),
]

