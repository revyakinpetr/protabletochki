import requests


def open_page_by_link(link, headers=None):
    if headers is None:
        headers = {
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }
    try:
        r = requests.get(link, headers=headers)
        return r.text
    except requests.exceptions.ConnectionError:
        print(link, "conn err")
        return ""
