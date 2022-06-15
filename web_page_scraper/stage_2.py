import re
import requests
from bs4 import BeautifulSoup


class Parser:
    @staticmethod
    def main_alg():
        link: str = input('Input the URL:\n> ')

        txt = requests.get(f'{link}', headers={'Accept-Language': 'en-US,en;q=0.5'})

        if txt.status_code != 200 or re.match(r'https://www.imdb.com/title/', link) is None:
            print("Invalid movie page!")
        else:
            soup = BeautifulSoup(txt.text, 'lxml')
            output = {}
            title = soup.title.text
            description = soup.find('span', class_="sc-16ede01-2 gXUyNh").text
            output["title"] = title
            output["description"] = description
            print(output)


p = Parser()
p.main_alg()
