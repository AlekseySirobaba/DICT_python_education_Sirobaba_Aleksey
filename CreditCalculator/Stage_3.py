import math


class Calculator:

    def __init__(self):
        self.principal = 0
        self.payment = 0
        self.interest = 0
        self.ir = 0
        self.months = 0

    def calc_n(self):
        years = 0

        # Input necessary data
        self.principal = int(input("Enter the loan principal:\n"))
        self.payment = int(input("Enter the monthly payment:\n"))
        self.interest = float(input("Enter the loan interest:\n"))

        # Calculates interest rate and how many months it takes to pay all loan
        self.ir = float(self.interest / (12 * 100))  # ir = interest rate
        self.months = math.ceil(math.log((self.payment / (self.payment - self.ir * self.principal)), 1 + self.ir))

        # Counts how many years the client will need to pay loan
        while self.months >= 12:
            years += 1
            self.months -= 12

        # Returning the result to the main body
        if years > 0:
            return f"It will take {years} years and {self.months} months to repay the loan"
        else:
            return f"It will take {self.months} months to repay the loan"

    def calc_a(self):
        self.principal = int(input("Enter the loan principal:\n"))
        self.months = int(input("Enter the number of months:\n"))
        self.interest = float(input("Enter the loan interest:\n"))

        self.ir = float(self.interest / (12 * 100))  # ir = interest rate

        self.payment = math.ceil(self.principal * ((self.ir * (1 + self.ir) ** self.months) /
                                 ((1 + self.ir) ** self.months - 1)))

        # Returning the result to the main body
        return f"Your monthly payment = {self.payment}"

    def calc_p(self):

        # Input necessary data
        self.payment = float(input("Enter the annuity payment:\n"))
        self.months = int(input("Enter the number of months:\n"))
        self.interest = float(input("Enter the loan interest:\n"))

        # Calculating interest rate and principal
        self.ir = float(self.interest / (12 * 100))  # ir = interest rate
        self.principal = math.floor(self.payment / ((self.ir * (1 + self.ir) ** self.months) /
                                    ((1 + self.ir) ** self.months - 1)))

        # Returning the result to the main body
        return f"Your loan principal = {self.principal}"


def main_body():

    result = ""
    while True:
        # Inputs the one of the action
        action = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:\n""")

        # Calling the method relying on chosen action or returns the message to type properly
        if action == 'n':
            result = commands.calc_n()
        elif action == 'a':
            result = commands.calc_a()
        elif action == 'p':
            result = commands.calc_p()
        else:
            print("\nPlease, type 'n', 'a' or 'p'")
            main_body()

        # Output of the results of calculating
        print(result)


# Starting the programme
if __name__ == "__main__":
    commands = Calculator()
    main_body()
