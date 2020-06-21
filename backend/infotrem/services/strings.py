import re
from typing import List


def break_string_into_words(original_str: str) -> List:
    name = original_str.upper().replace(" ", "_")
    return re.sub("_+", "_", name).split("_")
