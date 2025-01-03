from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    UpdateView, DeleteView, CreateView
)
from django.urls import reverse_lazy
from .models import Exercise

class ExerciseListView(ListView):
    model = Exercise
    template_name = "exercise_list.html"

class ExerciseDetailView(DetailView):
    model = Exercise
    template_name = "exercise_detail.html"

class ExerciseUpdateView(UpdateView):
    model = Exercise
    fields = (
        "exercise_name",
        "muscles_worked",
    )
    template_name = "exercise_edit.html"

class ExerciseDeleteView(DeleteView):
    model = Exercise
    template_name = "exercise_delete.html"
    success_url = reverse_lazy("exercise_list")

class ExerciseCreateView(CreateView):
    model = Exercise
    template_name = "exercise_new.html"
    fields = (
        "exercise_name",
        "muscles_worked",
        "author",
    )
# Create your views here.
