from api.mails.generic_mail import GenericMail
from core.models.contact.contact_model import Contact


class ContactMail(GenericMail):

    def __init__(self, obj: Contact):
        super(ContactMail, self).__init__()

        self.template = "mail/contact_mail.html"

        self.replace_dict = {
            'TYPE': obj.type,
            'NAME': obj.name,
            'CONTACT_EMAIL': obj.email,
            'CONTACT_PHONE': obj.phone,
            'MESSAGE': obj.message,
            'SENT_DATE': obj.created_at,
        }

    @staticmethod
    def get_raw_text() -> str:
        raw_text = "== CONTATO RECEBIDO PELO WEBSITE ==\n\n"

        raw_text += "Tipo: {{ TYPE }} \n"
        raw_text += "Nome: {{ NAME }} \n"
        raw_text += "E-mail: {{ CONTACT_EMAIL }} \n"
        raw_text += "Tel/Cel: {{ CONTACT_PHONE }} \n"
        raw_text += "Mensagem: {{ MESSAGE }} \n\n"
        raw_text += "Mensagem enviada em {{ SENT_DATE }} \n"

        return raw_text
