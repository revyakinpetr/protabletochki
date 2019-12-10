from bs4 import BeautifulSoup
from parse_drug_names import parse_drug_names
from open_page_by_link import open_page_by_link
from json_utils import save_json_to_file

WEBSITE_URL = 'https://drugchoice.vrachirf.ru'
WEBSITE_NAME = 'drugchoice'


def get_query_url(query):
    return f'{WEBSITE_URL}/seach?query={query}'


def get_drug_url(relative_drug_link):
    return f'{WEBSITE_URL}{relative_drug_link}'


def link_is_accurate(text, link):
    return text.lower() in link.text.lower()


def get_drugs_links(drug_name):
    query_url = get_query_url(drug_name)
    query_page = open_page_by_link(query_url)
    query_soup = BeautifulSoup(query_page, 'html.parser')
    drugs_links = query_soup.find_all('a', 'b-search-result__result-link')
    return drugs_links


def get_reviews(drug_link):
    drug_url = get_drug_url(drug_link.get('href'))
    drug_page = open_page_by_link(drug_url)
    drug_soup = BeautifulSoup(drug_page, 'html.parser')
    reviews = drug_soup.find_all('p', 'b-comment__description')
    reviews_json = []
    for review in reviews:
        reviews_json.append({'comment': review.get_text()})
    return reviews_json


def parse_drug_reviews(drug_name):
    """
    1. Get list of possible links to drug page
    2. Get link to reviews
    3. Extract needed data
    """
    reviews = []
    drugs_links = get_drugs_links(drug_name)
    for drug_link in drugs_links:
        if link_is_accurate(drug_name, drug_link):
            link_reviews = get_reviews(drug_link)
            reviews.extend(link_reviews)
    return reviews


if __name__ == "__main__":
    drug_names = parse_drug_names()
    for drug_name in drug_names:
        reviews_data = parse_drug_reviews(drug_name)
        if reviews_data:
            save_json_to_file(f'../data/{drug_name}_{WEBSITE_NAME}.json', reviews_data)
