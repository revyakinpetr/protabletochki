import os
from os.path import isfile, join
from json_utils import get_json_from_file, save_json_to_file
from parsers.path_utils import get_correct_path
from parsers.parse_drug_names import parse_drug_names

from pprint import pprint

DATA_DIR = os.getcwd()+'/data/'
DRUG_FILES = [
    f 
    for f in os.listdir(DATA_DIR) 
    if isfile(join(DATA_DIR, f))
]


if __name__ == "__main__":
    drug_side_effects = []
    path_to_drugs = get_correct_path(os.getcwd() + '/data/drugs_list.json')
    drug_names = parse_drug_names(path_to_drugs)

    DRUG_FILES.remove('meddra_all_se.txt')

    for drug_file in DRUG_FILES:
        if not drug_file.startswith('token_en_') and not drug_file.startswith('en_') and  not drug_file.startswith('drug'):
        # if drug_file.startswith('en_'):
            print(drug_file)
            path_to_drug_file = DATA_DIR + drug_file
            reviews_json = get_json_from_file(
                filename=path_to_drug_file
            )
            path_to_drug_file = DATA_DIR + 'en_' + drug_file
            reviews_json_en = get_json_from_file(
                filename=path_to_drug_file
            )
            count = len(reviews_json)
            print('Количества отзывов: {}'.format(count))

            for i in range(count):
                print('Номер {0}/{1}'.format(i+1, count))
                print(reviews_json[i])
                print(reviews_json_en[i])
                input()

