from googletrans import Translator
from json_utils import get_json_from_file, save_json_to_file

DEFAULT_DATA_SOURCE = 'data/drugs.json'
DEFAULT_DATA_DESTINATION = 'data/drugs_en.json'

DEFAULT_FROM_LANGUAGE = 'ru'
DEFAULT_TO_LANGUAGE = 'en'

REVIEW_FIELDS_TO_TRANSLATE = (
    'comment_plus',
    'comment_minus',
    'comment'
)


def source_text_invalid(text: str) -> bool:
    return text == ''


def translate(
        source_text: str,
        from_language: str = DEFAULT_FROM_LANGUAGE,
        to_language: str = DEFAULT_TO_LANGUAGE,
) -> str:

    if source_text_invalid(source_text):
        return source_text

    translator = Translator()
    translation = translator.translate(
        src=from_language,
        dest=to_language,
        text=source_text
    )
    return translation.text


def translate_reviews(
        drugs: dict,
) -> dict:
    for drug in drugs:
        for review in drug['reviews']:
            for field in review.keys():
                if field in REVIEW_FIELDS_TO_TRANSLATE:
                    review[field] = translate(review[field])
    return drugs


if __name__ == "__main__":

    drugs_json = get_json_from_file(
        filename=DEFAULT_DATA_SOURCE
    )

    translate_reviews(drugs_json)

    save_json_to_file(
        filename=DEFAULT_DATA_DESTINATION,
        data=drugs_json,
    )
