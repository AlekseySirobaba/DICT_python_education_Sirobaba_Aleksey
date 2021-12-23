import random


while True:
    options = ["Rock", "Paper", "Scissors"]
    win_conditions = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]

    while True:
        rps = input(">>> ")
        if rps in options:
            break
        else:
            pass

    comp_choice = random.choice(options)

    if win_conditions[options.index(rps)][options.index(comp_choice)] == 0:
        print(f"The re is a draw {comp_choice}")
    elif win_conditions[options.index(rps)][options.index(comp_choice)] == 1:
        print(f"Well done. The computer chose {comp_choice} and failed")
    elif win_conditions[options.index(rps)][options.index(comp_choice)] == -1:
        print(f"Sorry, but the computer chose {comp_choice}")
