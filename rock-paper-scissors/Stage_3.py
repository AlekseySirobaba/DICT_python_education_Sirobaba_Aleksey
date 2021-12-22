import random


class BestGame:

    def __init__(self):
        self.options = ["Rock", "Paper", "Scissors"]
        self.win_conditions = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
        self.rps = ""

    def input_player(self):
        self.rps = input(">>> ")
        if self.rps in self.options:
            game.main_body()
        elif self.rps == "!exit":
            print("Bye!")
            pass
        else:
            print("Invalid input")
            game.input_player()

    def main_body(self):
        comp_choice = random.choice(self.options)

        if self.win_conditions[self.options.index(self.rps)][self.options.index(comp_choice)] == 0:
            print(f"There is a draw {comp_choice}")
        elif self.win_conditions[self.options.index(self.rps)][self.options.index(comp_choice)] == 1:
            print(f"Well done. The computer chose {comp_choice} and failed")
        elif self.win_conditions[self.options.index(self.rps)][self.options.index(comp_choice)] == -1:
            print(f"Sorry, but the computer chose {comp_choice}")

        game.input_player()


def enter():
    action = input("Press Enter to continue")
    if action == "":
        game.input_player()
    else:
        enter()


if __name__ == "__main__":
    game = BestGame()
    enter()
