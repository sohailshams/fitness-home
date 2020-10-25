from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        """
        Telling django it is associated with review model
        """
        model = Review
        """
        Set exclude attribute and render all fields except user
        as it will never change
        """
        exclude = ('user',)
        """
        Override the default init method which allows the form
        to be customized
        """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        Remove auto-generated labels
        """
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0 review-input-form'
            field.label = False
            self.fields["your_review"].widget.attrs[
                                        "placeholder"] = "Your Review"
