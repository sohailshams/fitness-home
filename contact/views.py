from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import ContactForm


def contact(request):
    """
    View to handle the contact us email functionality
    """
    subject = render_to_string(
            'contact/contact_email/contact_email_subject.txt'
        )
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            full_name = request.POST.get('full_name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')

            try:
                send_mail(
                    subject,
                    message,
                    email,
                    [settings.DEFAULT_FROM_EMAIL],
                    )
                messages.success(request, 'Your query has been sent successfully!')
            except Exception as e:
                messages.error(request, f"Your query could not be sent,Error! {e}")
            """
            passed full_name in context to use it in contact_us.html
            """
            return render(request, 'contact/contact_us.html', {'full_name': full_name})
        else:
            messages.error(request,
                           'Sorry something went wrong, please make sure all fields are correctly filled out')
    else:
        form = ContactForm()

    template = 'contact/contact_us.html'
    context = {
        'form':form,
    }
    return render(request, template, context)

