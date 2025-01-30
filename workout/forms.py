from django import forms
from .models import Set

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