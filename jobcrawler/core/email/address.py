class EmailAddress:

    def __init__(self, email):
        self.email = email
        self._email_tpl = tuple(self._email.split('@'))

    def __str__(self):
        return self.email

    def __repr__(self):
        return f"{EmailAddress.__name__}('{self.email}')"

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = str(email)
        if not self._is_valid():
            raise ValueError(f'{self.email} is not a valid email address')

    @property
    def user(self):
        return self._email_tpl[0]

    @property
    def domain(self):
        return self._email_tpl[1]

    def _is_valid(self):
        email_split = self._email.split('@')
        if len(email_split) != 2:
            return False

        domain_split = email_split[1].split('.')
        if len(domain_split) < 2:
            return False

        return True
