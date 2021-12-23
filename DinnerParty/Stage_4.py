import random


def main_body(am_of_people, wil):
    lucky = " "  # Future name of lucky person
    names = []  # A list of names of joined people

    # Writes down in list input of the names of people who going to be on the party
    print("\nEnter the name of every friend (including you), each on a new line:")
    for _ in range(num_people):
        names.append(input())

    # Writes down the cost of the party
    amount = int(input("\nEnter the total amount:\n"))

    # Calculate how many each person should pay not/considering lucky person

    if wil is True:
        lucky = random.choice(names)
        print(f"\n{lucky} is the lucky one!")
        cash = round(amount / (am_of_people - 1), 2)
    else:
        cash = round(amount / am_of_people, 2)

    # Outputs the results of calculating
    print()
    list_of_people = dict.fromkeys(names, cash)
    if wil is True:
        list_of_people[lucky] = 0
    return list_of_people


try:
    # Writes down the input of the amount of people on the party
    num_people = int(input("Enter the number of friends joining (including you):\n"))
except (ValueError, ZeroDivisionError):
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
