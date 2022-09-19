import os

from api.mails.generic_mail import GenericMail
from core.models.user.user_model import User


class EmailConfirmation(GenericMail):

    def __init__(self, user: User):
        super(EmailConfirmation, self).__init__()

        self.template = "mail/email_validation_mail.html"

        self.replace_dict = {
            'NAME': str(user.name).split(maxsplit=1)[0],
            'VALIDATION_URL': self.get_validation_url(user=user),
        }

    @staticmethod
    def get_validation_url(user: User):
        return '{}/validate-email/{}/{}'.format(
            os.environ['FRONTEND_URL'],
            user.id,
            user.email_validation_hash
        )

    @staticmethod
    def get_raw_text() -> str:
        raw_text = """Olá {{ NAME }},
        
        Agradecemos por registrar-se no InfoTrem!
        
        Antes de poder enviar suas fotos e vídeos, você precisa validar seu e-mail.
        Para isso, acesse a URL abaixo em seu navegador:
        
        {{ VALIDATION_URL }}
        
        Se você não se cadastrou em nosso site e acredita que isto possa ser um engano, por favor contate-nos o quanto antes através do e-mail contato@infotrem.com.br
        
        Atenciosamente,
        Equipe InfoTrem
        """""

        return raw_text
