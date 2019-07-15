from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail, EmailMessage


def send_email(recipient_list, subject, template_name,
               from_email=settings.EMAIL_HOST_USER):

    html_message = render_to_string(template_name)
    message = strip_tags(html_message)

    return send_mail(subject, message, from_email, recipient_list, html_message=html_message)
