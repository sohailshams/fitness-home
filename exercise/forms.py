from django import forms
from .models import ExercisePlans


class ExerciseForm(forms.ModelForm):

    class Meta:
        model = ExercisePlans
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'
