import random


class Game:

    def __init__(self):
        self.options = ["Rock", "Paper", "Scissors"]
        self.win_conditions = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
        self.player_input = ""
        self.name = ""
        self.new_points = 0

    def info_player(self):
        self.name = input("Enter your name: ")
        print(f"Hello, {self.name}!")

        file = open("rating.txt")
        names_check = file.readlines()
        file.close()

        file = open("rating.txt", 'w')
        if not names_check:
            file.write(f"{self.name} 0")
            file.close()

        else:
            for key, line in enumerate(names_check):
                if self.name in line:
                    file.writelines(names_check)
                    file.close()
                    break

                elif self.name not in line and key == len(names_check) - 1:
                    names_check.append(f"\n{self.name} 0")
                    file.writelines(names_check)
                    file.close()
                    break

    def input_player(self):
        self.player_input = input(">>> ")
        if self.player_input in self.options:
            game.main_body()
        elif self.player_input == "!rating":
            game.rating_output()
        elif self.player_input == "!exit":
            print("Bye!")
            pass
        else:
            print("Invalid input")
            game.input_player()

    def inp_rating_doc(self):
        file = open("rating.txt")
        names_check = file.readlines()
        file.close()

        for key, line in enumerate(names_check):
            if self.name in line:
                list_str = list(names_check[key])

                number = ""
                delete = []
                for sym in list_str:
                    if sym.isnumeric():
                        number += sym
                        delete.append(sym)
                for del_sym in delete:
                    list_str.remove(del_sym)

                number = str(int(number) + self.new_points)

                if list_str[-1] == '\n':
                    list_str.insert(-1, number)
                else:
                    list_str.append(number)

                string = ''.join(list_str)
                names_check[key] = string

                file = open("rating.txt", 'w')
                file.writelines(names_check)
                file.close()

    def rating_output(self):
        file = open("rating.txt")
        names_check = file.readlines()

        for key, line in enumerate(names_check):
            if self.name in line:
                print(names_check[key])
                break
        game.input_player()

    def main_body(self):
        self.new_points = 0
        comp_choice = random.choice(self.options)

        if self.win_conditions[self.options.index(self.player_input)][self.options.index(comp_choice)] == 0:
            print(f"There is a draw {comp_choice}")
            self.new_points += 50

        elif self.win_conditions[self.options.index(self.player_input)][self.options.index(comp_choice)] == 1:
            print(f"Well done. The computer chose {comp_choice} and failed")
            self.new_points += 100

        elif self.win_conditions[self.options.index(self.player_input)][self.options.index(comp_choice)] == -1:
            print(f"Sorry, but the computer chose {comp_choice}")

        game.inp_rating_doc()
        game.input_player()


def enter():
    action = input("Press Enter to continue")
    if action == "":
        game.info_player()
        game.input_player()
    else:
        enter()


if __name__ == "__main__":
    game = Game()
    enter()
