from typing import List, Any
import requests

from transliterate import translit, slugify
from bs4 import BeautifulSoup

from parse_drug_names import parse_drug_names as pdn
from json_utils import save_json_to_file
from path_utils import get_correct_path
import parser_lib as parser


site = 'https://protabletky.ru'
site_name = 'protabletky'


def word_to_en(word: str) -> str:
	return slugify(word)


def list_to_en(words: List[str]) -> List[str]:
	words_en: List[str] = []
	for word in words:
		words_en.append(word_to_en(word))
	return words_en


def make_site_link(name: str) -> str:
	return '{0}/spb/find/?q={1}&obj=drug'.format(site, name)


def make_link(name: str) -> str:
	return 'https:{0}'.format(name)


def open_page(link: str) -> str:
	r = requests.get(link)
	if r.status_code == 200:
		return r.text
	return ''


def get_link(page: str) -> str:
	soup = BeautifulSoup(page, 'lxml')
	result_table = soup.find('table', {'class': 'lpu-list'})
	if not result_table:
		return ''
	href = result_table.find('a')
	if not href:
		return ''
	return href.get('href')


def save_reviews(name: str, reviews: List[Any]):
	name = get_correct_path(
		('../data/{0}_{1}.json').format(name, site_name)
	)
	save_json_to_file(name, reviews)


def get_list_of_pages(names):
	for name in names:
		search_page = open_page(make_site_link(name))
		href = get_link(search_page)
		if href != '':
			page = open_page(make_link(href))
			reviews = parser.get_reviews_by_page(page)
			save_reviews(name, reviews)


def parse():
	data_path = "../data/drugs_list.json"
	path = get_correct_path(data_path)
	drugs_ru = pdn(path)
	# drugs_en = list_to_en(drugs_ru)

	get_list_of_pages(drugs_ru)


if __name__ == '__main__':
    parse()
