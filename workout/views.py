from django.views.generic import(
    ListView, DetailView, UpdateView, DeleteView, 
    CreateView
)
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import WorkoutSession, Workout, Set
from .forms import CreateSetForm, CreateWorkoutForm

class WorkoutSessionListView(ListView):
    model = WorkoutSession
    template_name = "workout_session_list.html"

class WorkoutSessionDetailView(DetailView):
    model = WorkoutSession
    template_name = "workout_session_detail.html"
    pk_url_kwarg = "session_pk"

class WorkoutSessionCreateView(CreateView):
    model = WorkoutSession
    template_name = "workout_session_new.html"
    fields = (
        "workout_name",
        "author",
    )

class WorkoutSessionUpdateView(UpdateView):
    model = WorkoutSession
    fields = (
        "workout_name",
    )
    template_name = "workout_session_edit.html"
    pk_url_kwarg = "session_pk"
    
class WorkoutSessionDeleteView(DeleteView):
    model = WorkoutSession
    template_name = "workout_session_delete.html"
    pk_url_kwarg = "session_pk"
    success_url = reverse_lazy("workout_session_list")

class WorkoutSetUpdateView(UpdateView):
    model = Set
    fields = (
        "set_number",
        "repetitions",
        "weight",
        "notes",
    )
    template_name = "workout_set_edit.html"
    pk_url_kwarg = "set_pk"

    # def get_success_url(self):
    #     return reverse('workout_session_detail', kwargs={'session_pk':self.kwargs.get('session_pk')})

class WorkoutCreateView(CreateView):
    form_class = CreateWorkoutForm
    template_name = "workout_new.html"

    def get_initial(self):
        selected_workout_session = self.kwargs['session_pk']
        return {
            'workout_session': selected_workout_session,
        }

class WorkoutUpdateView(UpdateView):
    model = Workout
    form_class = CreateWorkoutForm
    template_name = "workout_edit.html"
    pk_url_kwarg = "workout_pk"

class WorkoutDeleteView(DeleteView):
    model = Workout
    template_name = "workout_delete.html"
    pk_url_kwarg = "workout_pk"
    
    def get_success_url(self):
        pk_from_before = self.get_object().workout_session
        return reverse_lazy("workout_session_detail", kwargs={'session_pk':pk_from_before.pk})

class WorkoutSetDeleteView(DeleteView):
    model = Set
    template_name = "workout_set_delete.html"
    pk_url_kwarg = 'set_pk'

    def get_success_url(self):
        pk_from_before = self.get_object().exercise.workout_session
        return reverse_lazy("workout_session_detail", kwargs={'session_pk':pk_from_before.pk})

class WorkoutSetCreateView(CreateView):
    form_class = CreateSetForm
    template_name = "workout_set_new.html"

    def get_initial(self):
        selected_exercise = self.kwargs['workout_pk']
        return {
            'exercise': selected_exercise,
        }
    
# Create your views here.