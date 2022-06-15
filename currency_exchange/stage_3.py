import requests
import json


class ValueConverter:
    @staticmethod
    def convert_alg():
        currency: str = input("> ")
        json_file = json.loads(requests.get(f"http://www.floatrates.com/daily/{currency}.json").text)
        usd_cur = json_file["usd"]["rate"]
        eur_cur = json_file["eur"]["rate"]
        print(f"Request on: {currency}, USD: {usd_cur}, EUR: {eur_cur}")


if __name__ == '__main__':
    v = ValueConverter()
    v.convert_alg()
