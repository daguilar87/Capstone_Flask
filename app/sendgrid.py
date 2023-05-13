import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

def send_email(from_email, to_emails, subject, content):
    message = Mail(
        from_email=from_email,
        to_emails=to_emails,
        subject=subject,
        html_content=content)
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    return response
