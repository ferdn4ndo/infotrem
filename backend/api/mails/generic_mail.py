from django.template.loader import render_to_string


class GenericMail:

    def __init__(self):
        self.replace_dict = {}
        self.template = "mail/dummy_mail.html"

    @staticmethod
    def get_raw_text() -> str:
        return "Hello World!"

    def parse_html(self) -> str:
        return render_to_string(self.template, self.replace_dict)

    def parse_raw(self) -> str:
        text = self.get_raw_text()
        for key, value in self.replace_dict.items():
            text.replace("{{ " + key + " }}", str(value))
        return text
