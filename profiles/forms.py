from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        """
        Telling django it is associated with user profile model
        """
        model = UserProfile
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
        """
        Add placeholders and classes, remove auto-generated
        labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_email': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
            }

        """
        Set auto focus on first field
        """

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-input-form'
            self.fields[field].label = False
