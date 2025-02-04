from django.views.generic import(
    ListView, DetailView, UpdateView, DeleteView, 
    CreateView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.urls import reverse_lazy
from .models import WorkoutSession, Workout, Set
from .forms import CreateSetForm, CreateWorkoutForm

class WorkoutSessionListView(LoginRequiredMixin, ListView):
    model = WorkoutSession
    template_name = "workout_session_list.html"

class WorkoutSessionDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = WorkoutSession
    template_name = "workout_session_detail.html"
    pk_url_kwarg = "session_pk"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class WorkoutSessionCreateView(LoginRequiredMixin, CreateView):
    model = WorkoutSession
    template_name = "workout_session_new.html"
    fields = ("workout_name",)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class WorkoutSessionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = WorkoutSession
    fields = (
        "workout_name",
    )
    template_name = "workout_session_edit.html"
    pk_url_kwarg = "session_pk"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class WorkoutSessionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = WorkoutSession
    template_name = "workout_session_delete.html"
    pk_url_kwarg = "session_pk"
    success_url = reverse_lazy("workout_session_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class WorkoutCreateView(LoginRequiredMixin, CreateView):
    form_class = CreateWorkoutForm
    template_name = "workout_new.html"

    def get_initial(self):
        selected_workout_session = self.kwargs['session_pk']
        return {
            'workout_session': selected_workout_session,
        }

class WorkoutUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Workout
    form_class = CreateWorkoutForm
    template_name = "workout_edit.html"
    pk_url_kwarg = "workout_pk"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class WorkoutDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Workout
    template_name = "workout_delete.html"
    pk_url_kwarg = "workout_pk"
    
    def get_success_url(self):
        pk_from_before = self.get_object().workout_session
        return reverse_lazy("workout_session_detail", kwargs={'session_pk':pk_from_before.pk})

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class WorkoutSetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Set
    fields = (
        "set_number",
        "repetitions",
        "weight",
        "notes",
    )
    template_name = "workout_set_edit.html"
    pk_url_kwarg = "set_pk"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class WorkoutSetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Set
    template_name = "workout_set_delete.html"
    pk_url_kwarg = 'set_pk'

    def get_success_url(self):
        pk_from_before = self.get_object().exercise.workout_session
        return reverse_lazy("workout_session_detail", kwargs={'session_pk':pk_from_before.pk})

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class WorkoutSetCreateView(LoginRequiredMixin, CreateView):
    form_class = CreateSetForm
    template_name = "workout_set_new.html"

    def get_initial(self):
        selected_exercise = self.kwargs['workout_pk']
        return {
            'exercise': selected_exercise,
        }
    
# Create your views here.