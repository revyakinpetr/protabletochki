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
	DRUG_FILES.remove('meddra_all_se.txt')

	for drug_file in DRUG_FILES:
		path_to_drug_file = DATA_DIR + drug_file
		drug_data = get_json_from_file(filename=path_to_drug_file)
		if len(drug_data) == 0:
			# Удалить файл
			os.remove(path_to_drug_file)
			print("Delete File: {0}".format(drug_file))