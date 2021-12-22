import random

options = ["Rock", "Paper", "Scissors"]

while True:
    rps = input()
    if rps == "Rock":
        print("Sorry, but the computer chose Paper")
    if rps == "Paper":
        print("Sorry, but the computer chose Scissors")
    if rps == "Scissors":
        print("Sorry, but the computer chose Rock")

