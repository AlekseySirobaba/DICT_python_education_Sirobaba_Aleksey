import requests


class Parser:
    @staticmethod
    def main_alg():
        link: str = input('Input the URL:\n> ')
        txt = requests.get(f'{link}')
        if txt.status_code != 200 or not txt.json()['content']:
            print("Invalid quote resource!")
        else:
            print(f"{txt.json()['content']}")


p = Parser()
p.main_alg()
