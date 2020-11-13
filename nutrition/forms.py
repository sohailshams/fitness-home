from django import forms
from .models import NutritionPlans


class NutritionForm(forms.ModelForm):

    class Meta:
        """
        Telling django it is associated with NutritionPlans model
        """
        model = NutritionPlans
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
