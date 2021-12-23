import random


class Domino:
    def __init__(self):
        self.dominoes = [[0, 0],
                         [0, 1], [1, 1],
                         [0, 2], [1, 2], [2, 2],
                         [0, 3], [1, 3], [2, 3], [3, 3],
                         [0, 4], [1, 4], [2, 4], [3, 4], [4, 4],
                         [0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5],
                         [0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6]
                         ]
        self.player = []
        self.computer = []
        self.stock = []
        self.snake = []
        self.status = ""

    # Creates a set of dominoes to computer and player
    def creating(self):
        # Creates the main massive of all 28 dominoes
        dominoes = self.dominoes.copy()

        # Gives 7 random dominoes to computer and player and removes these dominoes from main massive
        for piece in range(7):
            self.player.append(random.choice(dominoes))
            dominoes.remove(self.player[piece])
            self.computer.append(random.choice(dominoes))
            dominoes.remove(self.computer[piece])
        self.stock = dominoes.copy()
        game.game_conditions()

    # Checks if all conditions to play game are satisfied
    def game_conditions(self):

        # Finds in players sets first domino with same numbers to place and who`s first
        for i in range(7):
            if self.player[i][0] == self.player[i][1]:
                self.snake.append(self.player[i])
                self.player.remove(self.player[i])
                self.status = "Computer is about to make a move. Press Enter to continue..."
                game.output()
                break

            elif self.computer[i][0] == self.computer[i][1]:
                self.snake.append(self.computer[i])
                self.computer.remove(self.computer[i])
                self.status = "It's your turn to make a move. Enter your command."
                game.output()
                break

            # If there are no equal dominoes the algorithm
            else:
                game.__init__()
                game.creating()
                break

    # Outputs the result
    def output(self):
        print("=" * 70)  # Horizontal line
        print(f"""Stock size: {len(self.stock)}
Computer pieces: {len(self.computer)}\n""")  # Number of computer dominoes and in stock

        print(*self.snake)  # Game field

        print("\nYour pieces:")
        for key, elem in enumerate(self.player):    # Players dominoes
            print(key + 1, ":", elem, sep="")

        print(f"\nStatus: {self.status}\n")  # Status import random


class Domino:
    def __init__(self):
        self.dominoes = [[0, 0],
                         [0, 1], [1, 1],
                         [0, 2], [1, 2], [2, 2],
                         [0, 3], [1, 3], [2, 3], [3, 3],
                         [0, 4], [1, 4], [2, 4], [3, 4], [4, 4],
                         [0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5],
                         [0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6]
                         ]
        self.player = []
        self.computer = []
        self.stock = []
        self.snake = []
        self.status = ""

    # Creates a set of dominoes to computer and player
    def creating(self):
        # Creates the main massive of all 28 dominoes
        dominoes = self.dominoes.copy()

        # Gives 7 random dominoes to computer and player and removes these dominoes from main massive
        for piece in range(7):
            self.player.append(random.choice(dominoes))
            dominoes.remove(self.player[piece])
            self.computer.append(random.choice(dominoes))
            dominoes.remove(self.computer[piece])
        self.stock = dominoes.copy()
        game.game_conditions()

    # Checks if all conditions to play game are satisfied
    def game_conditions(self):

        # Finds in players sets first domino with same numbers to place and who`s first
        for i in range(7):
            if self.player[i][0] == self.player[i][1]:
                self.snake.append(self.player[i])
                self.player.remove(self.player[i])
                self.status = "Computer is about to make a move. Press Enter to continue..."
                game.output()
                break

            elif self.computer[i][0] == self.computer[i][1]:
                self.snake.append(self.computer[i])
                self.computer.remove(self.computer[i])
                self.status = "It's your turn to make a move. Enter your command."
                game.output()
                break

            # If there are no equal dominoes the algorithm
            else:
                game.__init__()
                game.creating()
                break

    # Outputs the result
    def output(self):
        print("=" * 70)  # Horizontal line
        print(f"""Stock size: {len(self.stock)}
Computer pieces: {len(self.computer)}\n""")  # Number of computer dominoes and in stock

        print(*self.snake)  # Game field

        print("\nYour pieces:")
        for key, elem in enumerate(self.player):    # Players dominoes
            print(key + 1, ":", elem, sep="")

        print(f"\nStatus: {self.status}\n")  # Status of the game

        menu()


# Game menu
def menu():
    game.__init__()
    action = input("""1. Play
0. Exit\n""")

    if action == '1':
        game.creating()
    elif action == '0':
        pass
    else:
        menu()


# Starts the programme
if __name__ == "__main__":
    game = Domino()
    menu()
