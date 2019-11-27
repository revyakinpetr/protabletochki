from json_utils import get_json_from_file, save_json_to_file
import nltk
import string
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer 

DEFAULT_DATA_SOURCE = 'drugs_en.json'
DEFAULT_DATA_DESTINATION = 'drugs_token.json'

REVIEW_FIELDS_TO_TOKENIZE = (
    'comment_plus',
    'comment_minus',
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
        drugs:dict,
):
    """Нормализация коментариев посредством удаления знаков пунктации, стоп слов, а также токенизация и лемматизация"""
    lemmatizer = WordNetLemmatizer()
    punctuation = string.punctuation
    punctuation += "''``"
    for drug in drugs:
        for review in drug['reviews']:
            for field in review.keys():
                if field in REVIEW_FIELDS_TO_TOKENIZE:
                    review[field] = nltk.word_tokenize(review[field])
                    review[field] = [i for i in review[field] if ( i not in punctuation )]
                    review[field] = [i for i in review[field] if ( i not in stopwords.words('english') )]

                    review[field] = [lemmatizer.lemmatize(i, get_wordnet_pos(i)) for i in review[field]]
    return drugs

if __name__ == "__main__":

    drugs_json = get_json_from_file(
        filename=DEFAULT_DATA_SOURCE
    )

    normalize_comments(drugs_json)

    save_json_to_file(
        filename=DEFAULT_DATA_DESTINATION,
        data=drugs_json,
    )