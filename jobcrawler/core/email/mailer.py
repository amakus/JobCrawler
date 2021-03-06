import smtplib
from typing import Tuple, List
from contextlib import contextmanager
from email.message import EmailMessage

from jobcrawler.core.email.credentials import EmailCredentials
from jobcrawler.core.email.content import HtmlContent
from jobcrawler.core.search.results import SearchResults


SMTP_HOSTS = {
        'gmail.com': ('smtp.gmail.com', 587),
        'outlook.com': ('smtp-mail.outlook.com', 587),
        'office365.com': ('smtp.office365.com', 587),
        'yahoo.com': ('smtp.mail.yahoo.com', 465),
        'web.de': ('smtp.web.de', 587),
        'hotmail.com': ('smtp.live.com', 465)
    }


class Mailer:
    """
    Class that sends job postings via email. Requires Gmail sender email account with 3rd party access rights.
    This can be done via https://myaccount.google.com/lesssecureapps.
    """

    def __init__(self, credentials, mail_to):
        # type: (Tuple[str, str], List[str])  -> None
        self.credentials = credentials
        self.mail_to = mail_to

    @property
    def credentials(self):
        return self._credentials

    @credentials.setter
    def credentials(self, cred):
        self._credentials = EmailCredentials(*cred)

    def send_search_results(self, search_results):
        # type: (List[SearchResults]) -> None

        msg = self.create_message(search_results)
        with email_server(self.credentials) as server:
            server.send_message(msg)

    def create_message(self, search_results):
        # type: (List[SearchResults]) -> EmailMessage

        msg = EmailMessage()
        msg['Subject'] = 'Jobs Update'
        msg['From'] = self._credentials.email
        msg['To'] = ', '.join([email for email in self.mail_to])

        content = HtmlContent(search_results)
        msg.set_content(content)

        return msg


@contextmanager
def email_server(credentails):
    """Context manager for easy setup and teardown of SMTP server."""

    smtp_host = SMTP_HOSTS.get(str(credentails.get_domain()))
    if not smtp_host:
        accepted_domains = ', '.join([k for k in SMTP_HOSTS.keys()])
        raise ValueError(f'Sender must use one of the following email domains: {accepted_domains}')

    server = smtplib.SMTP(*smtp_host)
    server.ehlo()
    server.starttls()

    try:
        server.login(*credentails)
    except smtplib.SMTPAuthenticationError:
        raise ValueError((f'Could not log into {str(credentails.email)} on SMTP Server {str(smtp_host)}. Check if '
                          '(1) you activated 3rd party access permissions and '
                          '(2) your email address and password are correct.'))

    try:
        yield server
    finally:
        server.quit()
