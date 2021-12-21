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
        self.turn = 0

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
                self.turn = 1  # Computers turn
                game.screen_output()
                break

            elif self.computer[i][0] == self.computer[i][1]:
                self.snake.append(self.computer[i])
                self.computer.remove(self.computer[i])
                self.status = "It's your turn to make a move. Enter your command."
                self.turn = 0  # Players turn
                game.screen_output()
                break

            # If there are no equal dominoes the algorithm
            else:
                game.__init__()
                game.creating()
                break

    # Switches turn between players
    def switch_players(self):
        if self.turn == 0:
            self.turn = 1  # Computers turn
            self.status = "Computer is about to make a move. Press Enter to continue..."
        elif self.turn == 1:
            self.turn = 0  # Players turn
            self.status = "It's your turn to make a move. Enter your command."

    def players_input(self):
        while True:
            # Player inputs his value
            dom_pos = input("> ")

            # Checks if value is number (positive/negative)
            if (dom_pos.isdigit() or '-' in dom_pos and dom_pos.strip('-')) \
                    and int(dom_pos) in range(-len(self.player), len(self.player) + 1):

                # Converting from string in int
                dom_pos = int(dom_pos)

                # If number is negative, then domino add to left side
                if dom_pos < 0:

                    dom_pos = abs(dom_pos)

                    # Selected domino is compared it`s values with the closest value in domino in snake
                    # If equal values aren't neighbours, than selected domino reversed
                    if self.player[dom_pos - 1][1] == self.snake[0][0]:
                        self.snake.insert(0, self.player[dom_pos - 1])
                        self.player.remove(self.player[dom_pos - 1])
                        break

                    elif self.player[dom_pos - 1][0] == self.snake[0][0]:
                        rev = list(self.player[dom_pos - 1])
                        rev.reverse()
                        self.snake.insert(0, rev)
                        self.player.remove(self.player[dom_pos - 1])
                        break

                    # If selected domino doesn't fit anywhere
                    else:
                        print("Illegal move. Please try again.")

                # If number is positive, then domino add to right side
                elif dom_pos > 0:

                    # Selected domino is compared it`s values with the closest value in domino in snake
                    # If equal values aren't neighbours, than selected domino reversed
                    if self.player[dom_pos - 1][1] == self.snake[-1][1]:
                        rev = list(self.player[dom_pos - 1])
                        rev.reverse()

                        self.snake.append(rev)
                        self.player.remove(self.player[dom_pos - 1])
                        break

                    elif self.player[dom_pos - 1][0] == self.snake[-1][1]:
                        self.snake.append(self.player[dom_pos - 1])
                        self.player.remove(self.player[dom_pos - 1])
                        break

                    # If selected domino doesn't fit anywhere
                    else:
                        print("Illegal move. Please try again.")

                # If number equal 0, then player takes random domino from stock
                elif dom_pos == 0:
                    self.player.append(random.choice(self.stock))
                    self.stock.remove(self.player[-1])
                    break
            else:
                print("Invalid input. Please try again.")  # If input value isn`t number

    def comp_input(self):
        while True:
            # Computer inputs random values considering how many dominoes it have and left or right side
            dom_pos = random.randint(-len(self.computer), len(self.computer))

            # If number is negative, then domino add to left side
            if dom_pos < 0:
                dom_pos = abs(dom_pos)

                # Selected domino is compared it`s values with the closest value in domino in snake
                # If equal values aren't neighbours, than selected domino reversed
                if self.computer[dom_pos - 1][1] == self.snake[0][0]:
                    self.snake.insert(0, self.computer[dom_pos - 1])
                    self.computer.remove(self.computer[dom_pos - 1])
                    break

                elif self.computer[dom_pos - 1][0] == self.snake[0][0]:
                    rev = list(self.computer[dom_pos - 1])
                    rev.reverse()
                    self.snake.insert(0, rev)
                    self.computer.remove(self.computer[dom_pos - 1])
                    break

            # If number is positive, then domino add to right side
            elif dom_pos > 0:

                # Selected domino is compared it`s values with the closest value in domino in snake
                # If equal values aren't neighbours, than selected domino reversed
                if self.computer[dom_pos - 1][1] == self.snake[-1][1]:
                    rev = list(self.computer[dom_pos - 1])
                    rev.reverse()

                    self.snake.append(rev)
                    self.computer.remove(self.computer[dom_pos - 1])
                    break

                elif self.computer[dom_pos - 1][0] == self.snake[-1][1]:
                    self.snake.append(self.computer[dom_pos - 1])
                    self.computer.remove(self.computer[dom_pos - 1])
                    break

            # If number equal 0, then computer takes random domino from stock
            elif dom_pos == 0:
                self.computer.append(random.choice(self.stock))
                self.stock.remove(self.computer[-1])
                break

            else:
                pass  # if domino doesn't fit, the loop continues

    # Outputs the result
    def screen_output(self):
        print("=" * 70)  # Horizontal line
        print(f"""Stock size: {len(self.stock)}
Computer pieces: {len(self.computer)}\n""")  # Number of computer dominoes and in stock

        if len(self.snake) > 6:
            print(*self.snake[0:3], "...", *self.snake[len(self.snake) - 3:], sep="")
        else: import random


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
        self.turn = 0

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
                self.turn = 1  # Computers turn
                game.screen_output()
                break

            elif self.computer[i][0] == self.computer[i][1]:
                self.snake.append(self.computer[i])
                self.computer.remove(self.computer[i])
                self.status = "It's your turn to make a move. Enter your command."
                self.turn = 0  # Players turn
                game.screen_output()
                break

            # If there are no equal dominoes the algorithm
            else:
                game.__init__()
                game.creating()
                break

    # Switches turn between players
    def switch_players(self):
        if self.turn == 0:
            self.turn = 1  # Computers turn
            self.status = "Computer is about to make a move. Press Enter to continue..."
        elif self.turn == 1:
            self.turn = 0  # Players turn
            self.status = "It's your turn to make a move. Enter your command."

    def players_input(self):
        while True:
            # Player inputs his value
            dom_pos = input("> ")

            # Checks if value is number (positive/negative)
            if (dom_pos.isdigit() or '-' in dom_pos and dom_pos.strip('-')) \
                    and int(dom_pos) in range(-len(self.player), len(self.player) + 1):

                # Converting from string in int
                dom_pos = int(dom_pos)

                # If number is negative, then domino add to left side
                if dom_pos < 0:

                    dom_pos = abs(dom_pos)

                    # Selected domino is compared it`s values with the closest value in domino in snake
                    # If equal values aren't neighbours, than selected domino reversed
                    if self.player[dom_pos - 1][1] == self.snake[0][0]:
                        self.snake.insert(0, self.player[dom_pos - 1])
                        self.player.remove(self.player[dom_pos - 1])
                        break

                    elif self.player[dom_pos - 1][0] == self.snake[0][0]:
                        rev = list(self.player[dom_pos - 1])
                        rev.reverse()
                        self.snake.insert(0, rev)
                        self.player.remove(self.player[dom_pos - 1])
                        break

                    # If selected domino doesn't fit anywhere
                    else:
                        print("Illegal move. Please try again.")

                # If number is positive, then domino add to right side
                elif dom_pos > 0:

                    # Selected domino is compared it`s values with the closest value in domino in snake
                    # If equal values aren't neighbours, than selected domino reversed
                    if self.player[dom_pos - 1][1] == self.snake[-1][1]:
                        rev = list(self.player[dom_pos - 1])
                        rev.reverse()

                        self.snake.append(rev)
                        self.player.remove(self.player[dom_pos - 1])
                        break

                    elif self.player[dom_pos - 1][0] == self.snake[-1][1]:
                        self.snake.append(self.player[dom_pos - 1])
                        self.player.remove(self.player[dom_pos - 1])
                        break

                    # If selected domino doesn't fit anywhere
                    else:
                        print("Illegal move. Please try again.")

                # If number equal 0, then player takes random domino from stock
                elif dom_pos == 0:
                    self.player.append(random.choice(self.stock))
                    self.stock.remove(self.player[-1])
                    break
            else:
                print("Invalid input. Please try again.")  # If input value isn`t number

    def comp_input(self):
        while True:
            # Computer inputs random values considering how many dominoes it have and left or right side
            dom_pos = random.randint(-len(self.computer), len(self.computer))

            # If number is negative, then domino add to left side
            if dom_pos < 0:
                dom_pos = abs(dom_pos)

                # Selected domino is compared it`s values with the closest value in domino in snake
                # If equal values aren't neighbours, than selected domino reversed
                if self.computer[dom_pos - 1][1] == self.snake[0][0]:
                    self.snake.insert(0, self.computer[dom_pos - 1])
                    self.computer.remove(self.computer[dom_pos - 1])
                    break

                elif self.computer[dom_pos - 1][0] == self.snake[0][0]:
                    rev = list(self.computer[dom_pos - 1])
                    rev.reverse()
                    self.snake.insert(0, rev)
                    self.computer.remove(self.computer[dom_pos - 1])
                    break

            # If number is positive, then domino add to right side
            elif dom_pos > 0:

                # Selected domino is compared it`s values with the closest value in domino in snake
                # If equal values aren't neighbours, than selected domino reversed
                if self.computer[dom_pos - 1][1] == self.snake[-1][1]:
                    rev = list(self.computer[dom_pos - 1])
                    rev.reverse()

                    self.snake.append(rev)
                    self.computer.remove(self.computer[dom_pos - 1])
                    break

                elif self.computer[dom_pos - 1][0] == self.snake[-1][1]:
                    self.snake.append(self.computer[dom_pos - 1])
                    self.computer.remove(self.computer[dom_pos - 1])
                    break

            # If number equal 0, then computer takes random domino from stock
            elif dom_pos == 0:
                self.computer.append(random.choice(self.stock))
                self.stock.remove(self.computer[-1])
                break

            else:
                pass  # if domino doesn't fit, the loop continues

    # Outputs the result
    def screen_output(self):
        print("=" * 70)  # Horizontal line
        print(f"""Stock size: {len(self.stock)}
Computer pieces: {len(self.computer)}\n""")  # Number of computer dominoes and in stock

        if len(self.snake) > 6:
            print(*self.snake[0:3], "...", *self.snake[len(self.snake) - 3:], sep="")
        else:                                                                               # Game field
            print(*self.snake)

        print("\nYour pieces:")
        for key, elem in enumerate(self.player):    # Players dominoes
            print(key + 1, ":", elem, sep="")

        print(f"\nStatus: {self.status}")  # Status of the game

    # Checks the game status
    def res_analyze(self):
        if len(self.computer) == 0:  # Computer doesn't have any dominoes left and wins
            return -1
        if len(self.player) == 0:  # Player doesn't have any dominoes left and wins
            return 1

        # Checks if inner of domino snake is 8 dominoes length
        if len(self.snake) - 2 == 8:
            correctness = True
            # Checks if all neighbour numbers of dominoes are equal in snake
            for key, element in enumerate(self.snake):
                if element[0] != self.snake[key - 1][1] and key >= 1:
                    correctness = False

            # If all this conditions are satisfied then returns a draw
            if self.snake[0][0] == self.snake[-1][1] and correctness is True:
                return 0


# Game algorithm
def main_body():
    game.creating()  # Creates domino sets and stock, chooses who will be the first and outputs game screen

    while True:  # Main loop of the game

        # Gives "players" an opportunity to input values including present turn
        if game.turn == 0:
            game.players_input()

        elif game.turn == 1:
            while True:
                action = input("> ")  # Needs to press Enter to allow computer input values
                if action == "":
                    game.comp_input()
                    break
                else:
                    print("Press Enter")  # If Enter not pressed or pressed with unnecessary symbols, outputs message

        # Conditions that checks if the game is already finished. If it`s true, when outputs one of the results
        # and exit from loop
        if game.res_analyze() == 1:
            game.status = "The game is over. You won!\n"
            game.screen_output()
            break
        elif game.res_analyze() == -1:
            game.status = "The game is over. The computer won!\n"
            game.screen_output()
            break
        elif game.res_analyze() == 0:
            game.status = "The game is over. It's a draw!\n"
            game.screen_output()
            break

        game.switch_players()  # If game not end, turn changes and outputs current game interface
        game.screen_output()

    menu()  # If game ended it returns to main menu


# Game menu
def menu():
    game.__init__()
    action = input("""1. Play
0. Exit\n""")

    if action == '1':
        main_body()
    elif action == '0':
        pass
    else:
        menu()


# Starts the programme
if __name__ == "__main__":
    game = Domino()
    menu()
