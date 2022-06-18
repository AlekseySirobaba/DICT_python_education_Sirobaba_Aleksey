import requests


class Parser:
    @staticmethod
    def main_alg(link: str) -> str:
        try:
            link_check = requests.get(link).status_code
        except requests.exceptions.MissingSchema:
            return "The URL returned error requests.exceptions.MissingSchema: Invalid URL!"

        if link_check == 404:
            return "The URL returned 404!"

        txt = requests.get(f'{link}').content
        file = open('source.html', 'wb')
        file.write(txt)
        file.close()
        return "Content saved."


if __name__ == '__main__':
    p = Parser()
    print(p.main_alg(input('Input the URL:\n> ')))
