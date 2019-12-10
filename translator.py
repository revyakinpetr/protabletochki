from googletrans import Translator
from json_utils import get_json_from_file, save_json_to_file
from parsers.parse_drug_names import parse_drug_names
import os
from os.path import isfile, join

DATA_DIR = os.getcwd()+'/data/'
DRUG_FILES = [f for f in os.listdir(DATA_DIR) if isfile(join(DATA_DIR, f))]

DRUG_NAMES = parse_drug_names(drugs_list_filename=DATA_DIR+'drugs_list.json')

DEFAULT_FROM_LANGUAGE = 'ru'
DEFAULT_TO_LANGUAGE = 'en'

REVIEW_FIELDS_TO_TRANSLATE = (
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
        drug['comment'] = translate(drug['comment'])
    return drugs


if __name__ == "__main__":
    for drug_name in DRUG_NAMES:
        for drug_file in DRUG_FILES:
            if drug_file.startswith(drug_name):
                    drugs_json = get_json_from_file(
                        filename=DATA_DIR+drug_file
                    )

                    translate_reviews(drugs_json)

                    save_json_to_file(
                        filename=DATA_DIR+'en_'+drug_file,
                        data=drugs_json,
                    )
