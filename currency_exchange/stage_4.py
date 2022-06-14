import requests
import json


class ValueConverter:
    def __init__(self):
        self.__cache: dict = {}

    def main_alg(self):
        while True:
            cur1 = input('Setup the value, please: ')

            if cur1 == 'USD' or 'EUR':  # Doing an exception for this two values to prevent the conflict with setup
                break                   # this values to cache (can`t do the converting of USD to USD or EUR to EUR)

            if self.__get_curs(cur1, 'usd') is None:
                print("Sorry, type the right value")
            else:
                self.__get_curs(cur1, 'usd')
                self.__get_curs(cur1, 'eur')
                break

        while True:
            cur2: str = input('Type the value to exchange: ').lower()

            while True:
                try:
                    amount: float = float(input('Type the amount of money you have: '))
                except ValueError:
                    print("Please, type correct value with numbers")
                else:
                    break

            print("Checking the cache...")
            if cur2 not in self.__cache.keys():
                print("Sorry, but it is not in cache!")
                print(f"You received {self.__calculation(self.__get_curs(cur1, cur2), amount)} {cur2.upper()}")

            else:
                print("It is in cache!")
                print(f"You received {self.__calculation(self.__cache[cur2], amount)} {cur2.upper()}")

    def __get_curs(self, cur1: str, cur2: str) -> [int, None]:
        try:
            json_file = json.loads(requests.get(f"http://www.floatrates.com/daily/{cur1}.json").text)
        except json.decoder.JSONDecodeError:
            return None

        try:
            cur_val = json_file[cur2]["rate"]
        except KeyError:
            return None

        self.__cache[cur2] = cur_val
        return cur_val

    @staticmethod
    def __calculation(val_cur: [float, int], money: [float, int]) -> [float, int, str]:
        if val_cur is None:
            return "nothing, because this value is not exist or the same with first value -->"

        return round(val_cur * money, 2)


if __name__ == '__main__':
    v = ValueConverter()
    v.main_alg()
