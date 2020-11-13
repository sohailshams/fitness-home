from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        """
        Telling django it is associated with Product model
        """
        model = Product
        """Render all fields"""
        fields = '__all__'

    """
    Override the default init method which allows the form
    to be customized
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'
