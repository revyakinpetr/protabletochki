from json_utils import get_json_from_file, save_json_to_file
import nltk
import os
from os.path import isfile, join
from parsers.parse_drug_names import parse_drug_names
import string
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer

DATA_DIR = os.getcwd() + '/data/'
DRUG_FILES = [f for f in os.listdir(DATA_DIR) if isfile(join(DATA_DIR, f))]

DRUG_NAMES = parse_drug_names(drugs_list_filename=DATA_DIR + 'drugs_list.json')

REVIEW_FIELDS_TO_TOKENIZE = (
    'comment'
)


def get_wordnet_pos(word):
    """Получение части речи для лемматизации"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)


def normalize_comments(
        reviews: dict,
):
    """Нормализация коментариев посредством удаления знаков пунктации, стоп слов, а также токенизация и лемматизация"""
    lemmatizer = WordNetLemmatizer()
    punctuation = string.punctuation
    punctuation += "''``"
    for review in reviews:
        review['comment'] = nltk.word_tokenize(review['comment'])
        review['comment'] = [i for i in review['comment'] if (i not in punctuation)]
        review['comment'] = [i for i in review['comment'] if (i not in stopwords.words('english'))]
        review['comment'] = [lemmatizer.lemmatize(i, get_wordnet_pos(i)) for i in review['comment']]
    return reviews


if __name__ == "__main__":

    for drug_name in DRUG_NAMES:
        for drug_file in DRUG_FILES:
            if drug_file.startswith('en_'+drug_name):
                reviews_json = get_json_from_file(
                    filename=DATA_DIR+drug_file
                )

                normalize_comments(reviews_json)

                save_json_to_file(
                    filename=DATA_DIR+'token_' + drug_file,
                    data=reviews_json,
                )
