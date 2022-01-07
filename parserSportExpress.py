import unicodedata

import requests
from bs4 import BeautifulSoup

class SportExpress:
    def __init__(self, url):
        self.url = url
        self.__host = self.url.replace('//', '/').split('/')[1].replace('www.', '')

    def parse(self):
        html = self.__get_html()
        return self.__get_data(html.text)

    def __get_data(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('h3', class_='se-material__title')
        card = []
        for k, item in enumerate(items):
            if k > 10:
                break
            card.append({
                'title':  unicodedata.normalize("NFKD", str(item.get_text())).replace('\n', ''),
                'url': item.a.get('href')
            })
        print(card)
        return card

    def __get_html(self, params={}):
        r = requests.get(self.url, params=params)
        return r

if __name__ == '__main__':
    url = 'https://www.sport-express.ru/swimming/'
    SportExpress(url).parse()
