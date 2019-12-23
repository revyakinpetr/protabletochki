import os
from os.path import isfile, join
from json_utils import get_json_from_file
from parsers.path_utils import get_correct_path
from parsers.parse_drug_names import parse_drug_names

from pprint import pprint


DRUG_NAME = 'Аторвастатин'
DATA_DIR = os.getcwd()+'/data/'
DRUG_FILES = [
    f 
    for f in os.listdir(DATA_DIR) 
    if isfile(join(DATA_DIR, f))
]


with open(DATA_DIR+'meddra_all_se.txt', 'r') as f:
    SIDE_EFFECTS = f.readlines()


def get_drug_name_from_filename(filename):
    return filename.split('.')[0].split('_')[2]


def work_with_review(review, drug_name):
    drug_side_effects = []
    for side_effect in SIDE_EFFECTS:
        side_effect_normalize = side_effect.rstrip('\n').lower()
        if side_effect_normalize in review['comment']:
            # print('{0} has {1}'.format(drug_name, side_effect))
            drug_side_effects.append(side_effect_normalize)
    return drug_side_effects


def work_with_drug_file(drug_file):
    drug_name = get_drug_name_from_filename(drug_file)
    drug_side_effects = {'drug': drug_name, 'side_effects': []}
    # print(drug_file)
    path_to_drug_file = DATA_DIR + drug_file
    reviews_json = get_json_from_file(
        filename=path_to_drug_file
    )
    for review in reviews_json:
        drug_side_effects['side_effects'] += work_with_review(review, drug_name)
    return drug_side_effects


if __name__ == "__main__":
    drug_side_effects = []
    path_to_drugs = get_correct_path(os.getcwd() + '/data/drugs_list.json')
    drug_names = parse_drug_names(path_to_drugs)

    for drug_file in DRUG_FILES:
        if drug_file.startswith('token_en_'):
            drug_side_effects.append(work_with_drug_file(drug_file))

    pprint(drug_side_effects)