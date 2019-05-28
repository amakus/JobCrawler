import pytest
from collections import namedtuple
from jobcrawler.core.filter import SearchFilter
from jobcrawler.core.mailer import Mailer
from jobcrawler.core.crawlers.airbuscrawler import AirbusCrawler

pytest_plugins = ['jobcrawler/tests/data/fixtures/job_items']


def get_mail_credentials():
    """
    Retrieves local username and password for email server. Must set keyring credentials locally.
        
        >> import keyring
        >> keyring.set_password('jobcrawler_test_email', 'email', 'ENTER_EMAIL_ADDRESS')
        >> keyring.set_password('jobcrawler_test_email', 'password', 'ENTER_PASSWORD')
    
    """
    import keyring
    credentails = namedtuple('Credentials', ['email', 'password'])
    email = keyring.get_password('jobcrawler_test_email', 'email')
    password = keyring.get_password('jobcrawler_test_email', 'password')

    return credentails(email, password)


# @pytest.mark.skip("Live email; must set email credentials, see get_mail_credentails()")
def test_mailer(fake_job_items):
    jobs = fake_job_items
    creds = get_mail_credentials()

    mailer = Mailer(creds, [creds.email])
    mailer.send_jobs(jobs)

