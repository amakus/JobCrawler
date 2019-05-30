import pytest
from jobcrawler.core.email.address import EmailAddress


def test_instantiation():
    email = EmailAddress('fake@address.com')
    assert isinstance(email, EmailAddress)


def test_attribs():
    email = EmailAddress('fake@address.com')
    assert email.email == 'fake@address.com'
    assert email.user == 'fake'
    assert email.domain == 'address.com'


def test_str_repr():
    email = EmailAddress('fake@address.com')
    assert str(email) == 'fake@address.com'
    assert repr(email) == "EmailAddress('fake@address.com')"


def test_bad_email():

    with pytest.raises(ValueError):
        EmailAddress('fake@email')

    with pytest.raises(ValueError):
        EmailAddress('fake.email')


