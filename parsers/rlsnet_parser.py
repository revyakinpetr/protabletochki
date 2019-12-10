from bs4 import BeautifulSoup
from parse_drug_names import parse_drug_names
from open_page_by_link import open_page_by_link
from transliterate import slugify
from json_utils import save_json_to_file

WEBSITE_URL = 'https://www.rlsnet.ru'
WEBSITE_NAME = 'rlsnet'


def get_reviews_url(drug_name):
    return f'{WEBSITE_URL}/comment/{drug_name}'


def parse_drug_reviews(drug_name):
    """
    1. Get reviews url
    2. Parse reviews
    """
    reviews = []
    drug_name_en = slugify(drug_name)
    reviews_link = get_reviews_url(drug_name_en)
    page = open_page_by_link(reviews_link)
    soup = BeautifulSoup(page, 'html.parser')
    reviews_list = soup.find_all('div', 'comment_text')
    for review in reviews_list:
        reviews.append({'comment': review.get_text()})
    return reviews


if __name__ == "__main__":
    drug_names = parse_drug_names()
    for drug_name in drug_names:
        reviews_data = parse_drug_reviews(drug_name)
        if reviews_data:
            save_json_to_file(f'../data/{drug_name}_{WEBSITE_NAME}.json', reviews_data)
