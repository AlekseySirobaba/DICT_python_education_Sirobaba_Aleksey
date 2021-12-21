import numpy as np


class GameTicTacToe:

    def __init__(self, list_of_letters):
        self.coordinates = []

        # Creates some 2D massive to create the matrix
        self.cell_pos = np.full((4, 4), 0, str)

        # Input the symbols from list into massive
        self.i = 1
        self.j = 1
        for element in list_of_letters:
            self.cell_pos[self.i][self.j] = element
            self.j += 1

            if self.j > 3:
                self.i += 1
                self.j = 1

    def screen(self):
        # Outputs the game field on the screen
        print(f"""        ---------
        | {self.cell_pos[1, 1]} {self.cell_pos[1, 2]} {self.cell_pos[1, 3]} |
        | {self.cell_pos[2, 1]} {self.cell_pos[2, 2]} {self.cell_pos[2, 3]} |
        | {self.cell_pos[3, 1]} {self.cell_pos[3, 2]} {self.cell_pos[3, 3]} |
        ---------""")

    def players_move(self):
        while True:
            # Writes down in variable coordinates that are typed in console
            self.coordinates = input("Enter the coordinates: ").split()

            # Checking the correctness of input
            commands.conditions()
            answer = commands.conditions()

            # If all requirements are satisfied, then the symbol X is staying on the position,
            # according to the entered coordinates
            if answer is True:
                self.i, self.j = map(int, self.coordinates)
                self.cell_pos[self.i, self.j] = 'X'
                break

    def conditions(self):
        # Checks if symbols are numbers
        if not str(self.coordinates[0]).isdigit() or not str(self.coordinates[1]).isdigit():
            return "You should enter numbers!"

        # Convert string symbols into numbers
        self.i, self.j = map(int, self.coordinates)

        # Checks the range of entered numbers
        if self.i not in range(1, 4) or self.j not in range(1, 4):
            return "Coordinates should be from 1 to 3."
        # Checks if cell isn`t occupied (empty)
        elif self.cell_pos[self.i, self.j] != '_':
            return "This cell is occupied! Choose another one!"
        # If all is good, then it gives ability to input the symbol on it`s exact position
        else:
            return True

    def game(self):
        # Values that counts the number of X and O on playing field
        counter_x = 0
        counter_o = 0

        # Lists which contains bool values about if there are 3 'X' or 3 'O' combinations
        win_condition_x = []
        win_condition_o = []

        for counter in range(1, 4):

            # These two commands read the columns and lines of gaming field and writes the result in the list
            values_h = (self.cell_pos[counter, 1:].tolist())
            values_v = (self.cell_pos[1:, counter].tolist())

            # Checks the data on 3 "X" or "3" "O" combinations and writes down the result
            win_condition_x.append(bool(values_h == ['X', 'X', 'X'] or values_v == ['X', 'X', 'X']))
            win_condition_o.append(bool(values_h == ['O', 'O', 'O'] or values_v == ['O', 'O', 'O']))

            # Counts the number of X and O on gaming field
            if counter_x == 0 or counter_o == 0:
                for symbol in self.cell_pos:
                    if any(symbol == 'X'):
                        counter_x += 1
                    if any(symbol == 'O'):
                        counter_o += 1

        # Returns winning or other game status
        if abs(counter_x - counter_o) >= 2 or True in win_condition_o and True in win_condition_x:
            return "Impossible\n"
        elif True in win_condition_x:
            return "X wins\n"
        elif True in win_condition_o:
            return "O wins\n"
        elif '_' in self.cell_pos:
            return "Game not finished\n"
        else:
            return "Draw\n"


# The algorithm of the game
while True:
    # Setups the position of symbols
    commands = GameTicTacToe(list("_XXOO_OX_"))

    # Outputs game field on the screen
    commands.screen()

    # Allows the player to input one symbol on game field
    commands.players_move()

    # Outputs updated game field
    commands.screen()

    # Outputs the status of whole game
    result = commands.game()
    print(result)

    # A slice for visual comfort
    print("------------------------------------")
