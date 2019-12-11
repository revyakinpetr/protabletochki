import os
from os.path import isfile, join
from json_utils import get_json_from_file


DRUG_NAME = 'Аторвастатин'
DATA_DIR = os.getcwd()+'/../data/'
DRUG_FILES = [f for f in os.listdir(DATA_DIR) if isfile(join(DATA_DIR, f))]

with open(DATA_DIR+'meddra_all_se.txt', 'r') as f:
    SIDE_EFFECTS = f.readlines()

if __name__ == "__main__":
    drug_side_effects = []
    for drug_file in DRUG_FILES:
        if drug_file.startswith('token_en_'+DRUG_NAME):
            print(drug_file)
            reviews_json = get_json_from_file(
                filename=DATA_DIR + drug_file
            )
            for review in reviews_json:
                for word in review['comment']:
                    for side_effect in SIDE_EFFECTS:
                        if word == side_effect.rstrip('\n').lower():
                            print(DRUG_NAME+' has '+side_effect)
                            drug_side_effects.append(side_effect)
