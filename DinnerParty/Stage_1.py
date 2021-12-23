list_of_people = {}  # Dict of people names who going to be on a party and how many each person should pay
names = []  # A list of names of joined people

# Writes down the input of the amount of people on the party
num_people = int(input("Enter the number of friends joining (including you):\n"))

# If number of people is 0 or less, then it considers like no one going to join the party and pay money
if num_people <= 0:
    print("No one is joining for the party")
else:
    # Else someone goes on party, then the costs are shared between these people
    print("Enter the name of every friend (including you), each on a new line:")

    # Writes down in list input of the names of people who going to be on the party
    for _ in range(num_people):
        names.append(input())

    # Outputs the results of calculating
    list_of_people = dict.fromkeys(names, 0)
    print(list_of_people)
