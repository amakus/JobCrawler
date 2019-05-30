from jobcrawler.core.email.address import EmailAddress


class EmailCredentials:

    def __init__(self, email, password):
        self._cred_tpl = (EmailAddress(email), str(password))

    def __getitem__(self, item):
        return str(self._cred_tpl[item])

    @property
    def email(self):
        return self._cred_tpl[0]

    @property
    def password(self):
        return self._cred_tpl[1]

    def get_domain(self):
        return self.email.domain
