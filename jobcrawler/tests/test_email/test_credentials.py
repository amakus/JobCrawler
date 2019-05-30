import pytest
from jobcrawler.core.email.credentials import EmailCredentials
from jobcrawler.core.email.address import EmailAddress


def test_instantiation():
    cred = EmailCredentials('fake@email.com', 'fake_password')
    assert isinstance(cred, EmailCredentials)


def test_has_attribs():
    cred = EmailCredentials('fake@email.com', 'fake_password')

    assert cred[0] == 'fake@email.com'
    assert str(cred.email) == 'fake@email.com'
    assert isinstance(cred.email, EmailAddress)

    assert cred[1] == 'fake_password'
    assert cred.password == 'fake_password'


def test_get_domain():
    cred = EmailCredentials('fake@email.com', 'fake_password')

    assert cred.get_domain() == 'email.com'
