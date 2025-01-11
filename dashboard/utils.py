from django.template.loader import render_to_string
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
from django.conf import settings


def send_email(to_email, subject, html_content):
    """
    Send email using sendgrid
    """
    message = Mail(
        from_email='cody@useexplore.com',
        to_emails=to_email,
        subject=subject,
        html_content=html_content
    )

    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return response.status_code

    except Exception as e:
        return str(e)


def email_questionnaire(user, link):
    """email test"""
    to_email = user.email
    subject = 'CPA Questionnaire'
    context = {
        "username": user.username,
        "link": link
    }
    html_message = render_to_string("dashboard/email_template.html", context=context)
    send_email(to_email, subject, html_message)
