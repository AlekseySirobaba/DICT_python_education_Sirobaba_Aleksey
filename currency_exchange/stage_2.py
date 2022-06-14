class ValueConverter:
    def __init__(self):
        self.ZLT: float = 0.23
        self.UAH: float = 1.02
        self.CAD: float = 0.55
        self.GBP: float = 1.513

    def convert_alg(self):
        amount: float = float(input("> "))
        print(f"""I will get {round(self.ZLT * amount, 2)} ZLT from the sale of {amount} dogecoins.
I will get {round(self.UAH * amount, 2)} UAH from the sale of {amount} dogecoins.
I will get {round(self.CAD * amount, 2)} CAD from the sale of {amount} dogecoins.
I will get {round(self.GBP * amount, 2)} GBP from the sale of {amount} dogecoins.""")


if __name__ == '__main__':
    v = ValueConverter()
    v.convert_alg()
