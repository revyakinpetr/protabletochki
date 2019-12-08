import requests

from bs4 import BeautifulSoup

from json_utils import save_json_to_file


def open_page_by_link(link):
    r = requests.get(link)
    return r.text


def get_reviews(page):
    soup = BeautifulSoup(page, 'lxml')
    main_reviews_list = soup.find('div', {'id': 'main'})
    review_list = main_reviews_list.find_all('tr', {'class': 'rate'})
    return review_list


def get_review_author_name(review):
    author = review.find('span', {'itemprop': 'name'})
    if author:
        return author.text
    return ''


def get_review_datetime(review):
    return review.find('div', {'class': 'datetime'}).text


def get_review_comment_plus(review):
    comment = review.find('p', {'class': 'comment_plus'})
    if comment:
        return comment.text
    return ''


def get_review_comment_minus(review):
    comment = review.find('p', {'class': 'comment_minus'})
    if comment:
        return comment.text
    return ''


def get_review_comment(review):
    comment = review.find('p', {'class': 'comment'})
    if comment:
        return comment.text
    comment = review.find('p', {'class': 'comment2'})
    if comment:
        return comment.text
    return ''


def get_json_review(review):
    author_name = get_review_author_name(review)
    datetime = get_review_datetime(review)
    comment_plus = get_review_comment_plus(review)
    comment_minus = get_review_comment_minus(review)
    comment = get_review_comment(review)

    return {
        'author_name': author_name,
        'is_specialist': author_name != '',
        'comment_plus': comment_plus,
        'comment_minus': comment_minus,
        'comment': comment
    }


def parse():
    file_text = []

    # Получаем список лекарств.

    # Получаем список страниц лекарств

    drug_link = 'https://protabletky.ru/atarax/'
    drug_info = {
        'name': 'atarax',
        'reviews': []
    }
    file_text.append(drug_info)

    # Открываем страницу лекарства
    drug_page = open_page_by_link(drug_link)

    # Получаем список отзывов на лекарство
    review_list = get_reviews(drug_page)

    # Достаем объекты отзыва
    for review in review_list:
        json_review = get_json_review(review)
        file_text[len(file_text) - 1]['reviews'].append(json_review)
        # Сохраняем в файл
        save_json_to_file('data/drugs.json', file_text)


if __name__ == '__main__':
    parse()
