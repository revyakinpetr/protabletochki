from bs4 import BeautifulSoup

from parsers.parser import open_page_by_link
from pprint import pprint


def get_drugs(page):
    soup = BeautifulSoup(page, 'lxml')
    drugs_list = soup.find('table', {'class': 'drug_list'})
    return drugs_list.find_all('tr', {'class': 'drug_list__drug'})


def get_name(drug):
    return drug.find('a', {'class': 'drug_list__drug_name'}).text


def get_link(drug):
    return drug.find('a', {'class': 'drug_list__drug_name'}).get('href')


def get_comment_number(drug):

    comments =  drug.find('a', {'class': 'drug_list__rates_count'})
    if not comments:
        return '0'
    return comments.text.split()[0]


def parse():
    absolute_link = 'https://protabletky.ru'
    disease_page = absolute_link + '/ot-gipertonii/'
    page = open_page_by_link(disease_page)
    drugs = get_drugs(page)
    result = []

    for drug in drugs:
        name = get_name(drug).strip()
        link = absolute_link + get_link(drug)
        comment_number = get_comment_number(drug).strip()
        result.append((name, link, comment_number))

    result.sort(key=lambda r: int(r[2]), reverse=True)
    pprint(result[:8])


if __name__ == '__main__':
    parse()
