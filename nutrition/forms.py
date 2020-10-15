from django import forms
from .models import NutritionPlans


class NutritionForm(forms.ModelForm):

    class Meta:
        model = NutritionPlans
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'
