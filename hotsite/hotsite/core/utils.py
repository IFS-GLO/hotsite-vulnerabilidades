from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage


def send_email(recipient_list, subject, template_name,
               from_email=settings.EMAIL_HOST_USER):
    message = render_to_string(template_name)

    return send_mail(subject, message, from_email, recipient_list,
                     auth_user=settings.EMAIL_HOST_USER, html_message=True)
