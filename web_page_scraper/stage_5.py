import string
import os
import pickle
import requests
from bs4 import BeautifulSoup


class Parser:
    def main_alg(self, type_article: str, max_page_num) -> bool:

        for page_num in range(1, int(max_page_num) + 1):
            url = f"https://www.nature.com/nature/articles?sort=PubDate&year=2022&page={page_num}"
            main_page = self.__parse_main_page(url)
            article_body = main_page.find('ul', class_='app-article-list-row')
            os.mkdir(f'Page_{page_num}')

            for row in article_body.find_all('li', class_="app-article-list-row__item"):
                if self.__article_type_check(row, type_article):
                    file_info = self.__parse_article_info(row)
                    self.__save_to_file(page_num, file_info[0], file_info[1])

        return True

    @staticmethod
    def __parse_main_page(link):
        main_body = requests.get(link).text
        main_txt = BeautifulSoup(main_body, 'html5lib')
        return main_txt

    @staticmethod
    def __article_type_check(article_body, searched_type):
        current_type = article_body.find('span', class_="c-meta__type").text
        if current_type == searched_type:
            return True
        else:
            return False

    @staticmethod
    def __parse_article_info(article_body):
        article_link = article_body.find('a', class_="c-card__link u-link-inherit")['href']
        article_body = BeautifulSoup(requests.get(f"https://www.nature.com{article_link}").text, 'lxml')
        output = {}

        output['title'] = article_body.find('h1', class_="c-article-magazine-title").text
        output['main text'] = article_body.find('div', class_="c-article-teaser-text").text.strip()

        return [output, output['title']]

    @staticmethod
    def __save_to_file(page_num, text, f_name):
        under_dash = str.maketrans(' ', '_')
        rm = [el for el in f_name if el in string.punctuation]
        for el in rm:
            f_name = f_name.replace(el, '')
        f_name = f_name.translate(under_dash)

        file = open(f'Page_{page_num}/{f_name}.txt', 'wb')
        pickle.dump(text, file)
        file.close()


if __name__ == '__main__':
    p = Parser()
    print(p.main_alg(input('> '), input('> ')))
