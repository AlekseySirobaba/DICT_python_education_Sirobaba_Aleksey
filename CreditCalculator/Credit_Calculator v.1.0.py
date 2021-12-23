import math
from argparse import ArgumentParser


class Calculator:

    def __init__(self):
        self.type = ""
        self.principal = 0
        self.payment = 0
        self.interest = 0
        self.ir = 0
        self.months = 0

    def conditions(self, *args):

        # Checks how many variables was input and their sign in front of the number
        negative_num = False
        counter = 0
        for element in args:
            if element is not None:
                counter += 1

            if type(element) is int or type(element) is float:
                if element < 0:
                    negative_num = True

        # Input conditions (checks correction of input)
        if counter != 4:
            print("Incorrect parameters")
        elif self.type is None or self.type != "annuity" and self.type != "diff":
            print("Incorrect parameters")
        elif self.type == "diff" and self.payment is not None:
            print("Incorrect parameters")
        elif negative_num is True:
            print("Incorrect parameters")
        elif self.interest is None:
            print("Incorrect parameters")
        else:

            # Method choosing (what the programme needs to calculate)
            p = self.principal
            m = self.months
            a = self.payment

            print("before")
            print(f"p = {p}, m = {m}, a = {a}, i = {self.interest}")
            if self.type == "diff":
                commands.calc_diff()
            elif self.type == "annuity":
                if m is None:
                    print("calc_n")
                    commands.calc_n()
                if a is None:
                    print("calc_a")
                    commands.calc_a()
                if p is None:
                    print("calc_p")
                    commands.calc_p()

        # TODO:  Work on conditions (needed to know which method to choose and have some input conditions)

    def calc_diff(self):
        tpa = 0  # total payment amount
        cm = 1   # current month

        p = self.principal
        i = self.interest
        m = self.months

        self.ir = float(i / (12 * 100))  # ir = interest rate
        while cm <= m:
            diff = math.ceil(p / m + self.ir * (p - (p * (cm - 1) / m)))
            tpa += diff
            print(f"Month {cm}: payment is {diff}")
            cm += 1

        if tpa > p:
            print(f"\nOverpayment = {int(tpa - p)}")

    def calc_n(self):
        p = self.principal
        i = self.interest
        a = self.payment
        years = 0

        # Calculates interest rate and how many months it takes to pay all loan
        self.ir = float(i / (12 * 100))  # ir = interest rate
        self.months = math.ceil(math.log((a / (a - self.ir * p)), 1 + self.ir))

        # Counts how many years the client will need to pay loan
        while self.months >= 12:
            years += 1
            self.months -= 12

        # Returning the result to the main body
        if years > 0 and self.months > 0:
            print(f"It will take {years} years and {self.months} months to repay the loan")
        elif years > 0 and self.months == 0:
            print(f"It will take {years} years to repay the loan")
        elif years == 0:
            print(f"It will take {self.months} months to repay the loan")

        if self.months * a > p:
            print(f"Overpayment = {int(self.months * a - p)}")

    def calc_a(self):
        p = self.principal
        i = self.interest
        m = self.months

        self.ir = float(i / (12 * 100))  # ir = interest rate
        a = math.ceil(p * (self.ir * (1 + self.ir) ** m) / (((1 + self.ir) ** m) - 1))

        # Returning the result to the main body
        print(f"Your monthly payment = {a}")
        if m * a > p:
            print(f"Overpayment = {int(m * a - p)}")

    def calc_p(self):
        i = self.interest
        m = self.months
        a = self.payment

        # Calculating interest rate and principal
        self.ir = float(i / (12 * 100))  # ir = interest rate
        p = math.floor(a / ((self.ir * (1 + self.ir) ** m) / ((1 + self.ir) ** m - 1)))

        print(f"Your loan principal = {p}")
        if m * a > p:
            print(f"Overpayment = {int(m * a - p)}")


def main_body():
    cmd_input.add_argument("-t", "--type", type=str)
    cmd_input.add_argument("-pm", "--payment", type=float)
    cmd_input.add_argument("-pr", "--principal", type=float)
    cmd_input.add_argument("-m", "--months", type=int)
    cmd_input.add_argument("-i", "--interest", type=float)
    args = cmd_input.parse_args()

    commands.type = args.type
    commands.payment = args.payment
    commands.principal = args.principal
    commands.months = args.months
    commands.interest = args.interest

    commands.conditions(args.type, args.payment, args.principal, args.months, args.interest)


# Starting the programme
if __name__ == "__main__":
    cmd_input = ArgumentParser("Credit Calculator")
    commands = Calculator()
    main_body()
