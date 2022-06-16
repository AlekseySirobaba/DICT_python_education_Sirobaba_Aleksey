import string
import pickle
import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self):
        self.__final_output: list = []

    def main_alg(self, link: str) -> str:
        main_page = self.__parse_main_page(link)
        article_body = main_page.find('ul', class_='app-article-list-row')

        for row in article_body.find_all('li', class_="app-article-list-row__item"):
            if self.__article_type_check(row):
                file_info = self.__parse_article_info(row)
                self.__save_to_file(file_info[0], file_info[1])

        return f"Saved articles: {self.__final_output}"

    @staticmethod
    def __parse_main_page(link):
        main_body = requests.get(link).text
        main_txt = BeautifulSoup(main_body, 'html5lib')
        return main_txt

    @staticmethod
    def __article_type_check(article_body):
        article_type = article_body.find('span', class_="c-meta__type").text
        if article_type == "News":
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

    def __save_to_file(self, text, f_name):
        under_dash = str.maketrans(' ', '_')
        rm = [el for el in f_name if el in string.punctuation]
        for el in rm:
            f_name = f_name.replace(el, '')
        f_name = f_name.translate(under_dash)

        file = open(f'{f_name}.txt', 'wb')
        pickle.dump(text, file)
        file.close()
        self.__final_output.append(f'{f_name}.txt')


if __name__ == '__main__':
    p = Parser()
    print(p.main_alg("https://www.nature.com/nature/articles?type=news&year=2022"))
