import pytest
import keyring
from jobcrawler.core.filter import SearchFilter
from jobcrawler.core.mailer import Mailer
from jobcrawler.core.crawlers.airbuscrawler import AirbusCrawler

pytest_plugins = ['jobcrawler/tests/data/fixtures/job_items']


def get_mail_credentials():
    """
    Must set keyring credentials, then enter email below. Example:
        
        >> keyring.set_password('jobcrawler_test_email', 'EMAIL', 'PASSWORD')
    
    """"
    email = 'ENTER_EMAIL'
    password = keyring.get_password('jobcrawler_test_email', email)

    return email, password


@pytest.mark.skip("Must set email credentials; see function above")
def test_mailer(fake_job_items):
    creds = get_mail_credentials()
    jobs = fake_job_items

    mail_to = ['py.makus@gmail.com']
    mailer = Mailer(mail_to)
    mailer.send_jobs(jobs)

