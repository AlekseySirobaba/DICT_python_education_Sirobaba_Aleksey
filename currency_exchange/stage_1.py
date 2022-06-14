class ValueConverter:
    @staticmethod
    def convert_alg():
        amount: int = int(input("Please, enter the number of dogecoins you have: "))
        currency: float = float(input("Please, enter the exchange rate: "))
        print(f"The total amount of dollars: {amount * currency}")


if __name__ == '__main__':
    v = ValueConverter()
    v.convert_alg()
