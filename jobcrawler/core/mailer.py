import smtplib


class Mailer:

    def __init__(self, mail_to):
        self.mail_to = mail_to

    def send_jobs(self, job_items):
        SERVER = "localhost"

        FROM = "sender@example.com"
        TO = self.mail_to  # must be a list

        SUBJECT = "Hello!"

        TEXT = "This message was sent with Python's smtplib."

        # Prepare actual message

        message = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

        # Send the mail

        server = smtplib.SMTP(SERVER)
        server.sendmail(FROM, TO, message)
        server.quit()
