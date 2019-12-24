import json

from yandex_translate import YandexTranslate, YandexTranslateException
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

YANDEX_API_KEY = 'trnsl.1.1.20190324T122631Z.0b2111ddbf484dec.419078bb0fe5fcf6d9b58399981e028e9a20614a'
translator = YandexTranslate(YANDEX_API_KEY)


def source_text_invalid(text: str) -> bool:
    return text == ''


def translate(
        source_text: str,
        from_language: str = DEFAULT_FROM_LANGUAGE,
        to_language: str = DEFAULT_TO_LANGUAGE,
) -> str:

    if source_text_invalid(source_text):
        return source_text

    try:
        translation = translator.translate(
            source_text, to_language
        )
    except YandexTranslateException:
        translation = translator.translate(
            source_text[:300], to_language
        )
    return translation['text'][0]


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
                try:
                    translate_reviews(drugs_json)

                    save_json_to_file(
                        filename=DATA_DIR+'en_'+drug_file,
                        data=drugs_json,
                    )
                except json.decoder.JSONDecodeError:
                    print('error at ', drug_file)
