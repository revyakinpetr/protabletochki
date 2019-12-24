import glob
from typing import List, Any, Dict, Tuple

from json_utils import get_json_from_file
from path_utils import get_correct_path
from parse_drug_names import parse_drug_names as pdn


path_to_files = '../data/{drug}_*.json'


def find_files(path: str) -> List[str]:
    """Find and return python test files in path."""
    if path == '':
        path = '.'
    return glob.glob(path)


def count_file(file_name: str) -> int:
	file_name = get_correct_path(file_name)
	return len(get_json_from_file(file_name))


def count_files(file_names: List[str]) -> int:
	count_number = 0
	for file_name in file_names:
		count_number += count_file(file_name)
	return count_number


def count(names: List[str]) -> Dict[str, int]:
	counts: Dict[str, int] = {}
	for name in names:
		path = path_to_files.format(drug=name)
		file_names = find_files(path)
		count_number = count_files(file_names)
		counts[name] = count_number	
	return counts


def sort_dict(d: Dict[str, int]) -> List[Tuple]:
	return sorted(
			d.items(), 
			key=lambda item: (item[1], item[0])
		)


def main():
	data_path = "../data/drugs_list.json"
	path = get_correct_path(data_path)
	drugs = pdn(path)
	drug_count = count(drugs)
	drug_count_sort = sort_dict(drug_count)

	for drug in drug_count_sort[::-1]:
		out_str = '{name}: {count}'.format(name=drug[0], count=drug[1])
		print(out_str)


if __name__ == '__main__':
    main()
