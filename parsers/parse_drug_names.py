from json_utils import get_json_from_file


def parse_drug_names(drugs_list_filename: str = '../data/drugs_list.json') -> list:
    drugs_list = get_json_from_file(drugs_list_filename)
    drugs_names = []
    for pharm_group in drugs_list:
        for active_substance in pharm_group['pharmGroup']['activeSubstances']:
            for drug in active_substance['drugs']:
                drugs_names.append(drug['name'])
    return drugs_names
