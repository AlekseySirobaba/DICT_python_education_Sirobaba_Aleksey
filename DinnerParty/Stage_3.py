import random


def main_body(am_of_people, wil):  # who is lucky
    names = []  # A list of names of joined people

    # Writes down in list input of the names of people who going to be on the party
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_people):
        names.append(input())

    # If who is lucky (wil) feature turn on, then randomly choose a lucky person
    if wil is True:
        # Choosing the name of lucky person randomly
        lucky = random.choice(names)
        print(f"{lucky} is the lucky one!")

    # Writes down the cost of the party and calculate how many each person should pay
    amount = int(input("Enter the total amount:\n"))
    cash = round(amount / am_of_people, 2)

    # Outputs the results of calculating
    list_of_people = dict.fromkeys(names, cash)
    return list_of_people


try:
    # Writes down the input of the amount of people on the party
    num_people = int(input("Enter the number of friends joining (including you):\n"))
except ValueError:
    print("No one is joining for the party")
else:
    # If number of people is 0 or less, then it considers like no one going to join the party and pay money
    if num_people <= 0:
        print("No one is joining for the party")
    else:
        action = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if action == "Yes":
            lucky_feature = True
        else:
            lucky_feature = False
            print("No one is going to be lucky")

        # Else someone goes on party, then the costs are shared between these people
        print(main_body(num_people, lucky_feature))
