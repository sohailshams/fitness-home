from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

    """
    Override the default init method which allows the form
    to be customized
    """
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        """
        Remove auto-generated labels & added placeholders
        """
        for field in self.fields:
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = 'rounded-0'
            self.fields["full_name"].widget.attrs[
                                        "placeholder"] = "Name *"
            self.fields["email"].widget.attrs[
                                        "placeholder"] = "Email Address *"
            self.fields["message"].widget.attrs[
                                        "placeholder"] = "Your Query *"
