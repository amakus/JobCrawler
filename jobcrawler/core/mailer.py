import smtplib
from contextlib import contextmanager
from email.message import EmailMessage
from typing import Tuple, List


class Mailer:
    """
    Class that sends job postings via email. Requires Gmail sender email account with 3rd party access rights.
    This can be done via https://myaccount.google.com/lesssecureapps.
    """

    def __init__(self, credentials, mail_to):
        # type: (Tuple[str, str], List[str])  -> None
        self.credentails = credentials
        self.mail_to = mail_to

    @property
    def credentials(self):
        return self._credentials

    @credentials.setter
    def credentials(self, cred):
        email_domain = cred[0].split('@')[1]
        if email_domain is not 'gmail.com':
            raise IOError('Sender must use Gmail (@gmail.com)')

    def send_jobs(self, job_items):
        msg = self._create_message(job_items)
        with gmail_server(self.credentails) as server:
            server.send_message(msg)

    def _create_message(self, job_items):
        msg = EmailMessage()
        msg['Subject'] = 'Jobs Update'
        msg['From'] = self.credentails[0]
        msg['To'] = ', '.join([email for email in self.mail_to])

        content = self._make_content(job_items)
        msg.set_content(content)

        return msg

    def _make_content(self, job_items):
        return ' '


@contextmanager
def gmail_server(credentails):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    try:
        server.login(*credentails)
    except smtplib.SMTPAuthenticationError:
        raise IOError()

    try:
        yield server
    finally:
        server.quit()
