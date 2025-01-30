from django import forms
from .models import Set, Workout

class CreateSetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateSetForm, self).__init__(*args, **kwargs)
        self.fields['exercise'].disabled = True

    class Meta:
        model = Set
        fields = (
            "exercise",
            "set_number",
            "repetitions",
            "weight",
            "notes",
        )

class CreateWorkoutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateWorkoutForm, self).__init__(*args, **kwargs)
        self.fields['workout_session'].disabled = True

    class Meta:
        model = Workout
        fields = (
            "workout_session",
            "exercise",
        )