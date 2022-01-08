import requests
from bs4 import BeautifulSoup


class SportBox:
    def __init__(self, url):
        self.url = url
        self.__host = self.url.replace('//', '/').split('/')[1].replace('www.', '')

    def parse(self):
        html = self.__get_html()
        return self.__get_data(html.text)

    def __get_data(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('a', class_='title')
        card = []
        for item in items:
            card.append({
                'title': item.get_text(),
                'url': self.__host + item.get('href')
            })
        print(card)
        return card

    def __get_html(self, params={}):
        r = requests.get(self.url, params=params)
        return r

if __name__ == '__main__':
    url = 'https://news.sportbox.ru/Vidy_sporta/plavanie'
    SportBox(url).parse()
