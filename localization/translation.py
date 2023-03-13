from config import phone_language
from localization.dictionary import serbian, english


def get_translation_for_key(key):
    match phone_language:
        case "sr":
            dictionary = serbian
        case _:
            dictionary = english

    return dictionary.get(key)
