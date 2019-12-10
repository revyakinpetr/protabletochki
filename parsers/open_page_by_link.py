import requests


def open_page_by_link(link):
    r = requests.get(link)
    return r.text
