from django import forms
from .models import ExercisePlans


class ExerciseForm(forms.ModelForm):

    class Meta:
        """
        Telling django it is associated with ExercisePlans model
        """
        model = ExercisePlans
        """Render all fields"""
        fields = '__all__'

    """
    Override the default init method which allows the form
    to be customized
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        """Add class"""
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'
