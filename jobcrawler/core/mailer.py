import smtplib
from dataclasses import dataclass
from enum import Enum
from contextlib import contextmanager
from email.message import EmailMessage
from typing import Tuple, List


class Mailer:
    """
    Class that sends job postings via email. Requires Gmail sender email account with 3rd party access rights.
    This can be done via https://myaccount.google.com/lesssecureapps.
    """

    _smpt_hosts = {
        'gmail.com': ('smtp.gmail.com', 587),
        'outlook.com': ('smtp-mail.outlook.com', 587),
        'office365.com': ('smtp.office365.com', 587),
        'yahoo.com': ('smtp.mail.yahoo.com', 465),
        'web.de': ('smtp.web.de', 587),
        'hotmail.com': ('smtp.live.com', 465)
    }

    def __init__(self, credentials, mail_to):
        # type: (Tuple[str, str], List[str])  -> None
        self.credentails = credentials
        self.mail_to = mail_to
        self._smpt_host = None

    @property
    def credentials(self):
        return self._credentials

    @credentials.setter
    def credentials(self, cred):
        email = EmailAddress(cred[0])
        try:
            email_domain = str(cred[0]).split('@')[1]
        except IndexError:
            raise IOError(f'{str(cred[0])} is not a valid email address')

        if email_domain not in self._smpt_hosts:
            accepted_domains = ', '.join([k for k in self._smpt_hosts.keys()])
            raise IOError(f'Sender must use one of the following domains: {accepted_domains}')

        self._smpt_host = self._smpt_hosts[email_domain]
        self._credentials = cred

    def send_jobs(self, job_items):
        msg = self._create_message(job_items)
        with email_server(self._smpt_host, self.credentails) as server:
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
def email_server(smtp_host, credentails):
    server = smtplib.SMTP(*smtp_host)
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


class EmailAddress:

    def __init__(self, email):
        self._email = str(email)
        if not self.is_valid():
            raise IOError(f'{self._email} is not a valid email address')

    @property
    def user(self):
        return self._email.split('@')[0]

    @property
    def domain(self):
        return self._email.split('@')[1]

    def is_valid(self):
        address_split = self._email.split('@')
        if not len(address_split) == 2:
            return False
        return True
