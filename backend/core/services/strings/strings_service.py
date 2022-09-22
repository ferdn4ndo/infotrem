import base64
import random
import re
import string
from typing import List


class StringsService:
    input_string: str = ""

    def __init__(self, input_string: str = ""):
        self.input_string = input_string

    def break_string_into_words(self) -> List:
        name = self.input_string.upper().replace(" ", "_")

        return re.sub("_+", "_", name).split("_")

    def generate_random_string(self) -> str:
        """ Generate a random string of letters and digits and special characters and base64 encode it """
        password_characters = self.input_string if self.input_string != "" else string.ascii_letters + string.digits

        return ''.join(random.choice(password_characters) for i in range(32))

    def generate_random_encoded_string(self) -> str:
        """ Generate a random string of letters and digits and special characters and base64 encode it """
        generated_key = self.generate_random_string()

        return str(base64.urlsafe_b64encode(generated_key.encode('utf-8')).decode('utf-8'))
