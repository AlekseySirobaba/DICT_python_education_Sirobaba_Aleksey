import math


def calc_m():
    # Input money to be paid for a month
    payment = int(input("Enter the monthly payment:\n"))
    # Calculates how many months it takes to pay all loan
    months = math.ceil(principal / payment)
    # Output the result on the screen
    print(f"It will take {months} months to repay the loan")


def calc_f():
    # Input the number of months to pay loan
    months = int(input("Enter the number of months:\n"))
    # Calculates amount of cash needs to be paid for a month
    payment = math.ceil(principal / months)

    # Calculates the last payment for comparison
    last_payment = principal - (months - 1) * payment

    # If the last payment is equal with payment per month, then it will output payment in one month in general
    # If not -- payment for all months and the last month singly
    if last_payment == payment:
        print(f"Your monthly payment = {payment}")
    else:
        print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")


while True:
    # Inputs the loan principal
    principal = int(input("Enter the loan principal:\n"))

    # Inputs the one of the action
    action = input("""What do you want to calculate?
type "m" – for number of monthly payments,
type "p" – for the monthly payment:\n""")

    # Calling the method relying on chosen action or returns the message to type properly
    if action == 'm':
        calc_m()
    elif action == 'p':
        calc_f()
    else:
        print("Please, type 'm' or 'p'")
