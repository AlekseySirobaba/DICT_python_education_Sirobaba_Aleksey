def main_body(am_of_people):
    names = []  # A list of names of joined people

    # Writes down in list input of the names of people who going to be on the party
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_people):
        names.append(input())

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
        # Else someone goes on party, then the costs are shared between these people
        print(main_body(num_people))
