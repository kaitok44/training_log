from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    UpdateView, DeleteView, CreateView
)
from django.urls import reverse_lazy
from .models import Exercise

class ExerciseListView(LoginRequiredMixin, ListView):
    model = Exercise
    template_name = "exercise_list.html"

class ExerciseDetailView(
    LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Exercise
    template_name = "exercise_detail.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ExerciseUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Exercise
    fields = (
        "exercise_name",
        "muscles_worked",
    )
    template_name = "exercise_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ExerciseDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Exercise
    template_name = "exercise_delete.html"
    success_url = reverse_lazy("exercise_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ExerciseCreateView(LoginRequiredMixin, CreateView):
    model = Exercise
    template_name = "exercise_new.html"
    fields = (
        "exercise_name",
        "muscles_worked",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
# Create your views here.
