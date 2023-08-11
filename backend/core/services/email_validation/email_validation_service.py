import os
import secrets

from core.mails.email_confirmation_mail import EmailConfirmation
from core.services.mailer.mailer_service import MailerService
from core.models.mail.mail_model import Mail
from core.models.user.user_model import User


class EmailValidationService:

    EMAIL_HASH_LENGTH = 32

    def __init__(self, user: User, debug=False):
        self.debug = debug
        self.user = user
        self.validated = user.email_validated
        self.validation_sent = user.email_validation_sent
        self.validation_hash = user.email_validation_hash
        self.mailer = MailerService()

    def send_new_validation_mail(self) -> bool:
        if self.user.email_validated:
            return False

        self.generate_hash()
        self.send_validation_mail()

        return True

    def generate_hash(self):
        self.user.email_validation_hash = secrets.token_hex(nbytes=self.EMAIL_HASH_LENGTH)
        self.user.email_validation_sent = False
        self.user.save()

    def send_validation_mail(self):
        self.generate_email()
        self.user.email_validation_sent = True
        self.user.save()

    def generate_email(self) -> Mail:
        mail = Mail()
        mail_template = EmailConfirmation(self.user)
        mail.to = self.user.email
        mail.subject = "Confirme seu e-mail no InfoTrem"
        mail.message_html = mail_template.parse_html()
        mail.message_text = mail_template.parse_raw()
        mail.reply_to = os.environ['EMAIL_SMTP_USER']
        mail.save()

        return mail

    def validate_user_hash(self, validation_hash: str) -> bool:
        if self.user.email_validation_hash == '' or self.user.email_validation_hash != validation_hash:
            return False

        if not self.user.email_validated:
            self.user.email_validated = True
            self.user.save()

        return True