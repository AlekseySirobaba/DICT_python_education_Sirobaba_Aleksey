import numpy as np


class GameTicTacToe:

    def __init__(self):
        self.coordinates = []
        self.turn = 0
        self.symbol = ' '

        # Creates some 2D massive to create the matrix
        self.cell_pos = np.full((4, 4), 0, str)

        # Input the symbols from list into massive
        self.i = 1
        self.j = 1
        for element in range(0, 9):
            self.cell_pos[self.i][self.j] = '_'
            self.j += 1
            if self.j > 3:
                self.i += 1
                self.j = 1

    def screen(self):
        #  Outputs some slice for visual comfort and game field
        print("=============")
        print(f"""---------
| {self.cell_pos[1, 1]} {self.cell_pos[1, 2]} {self.cell_pos[1, 3]} |
| {self.cell_pos[2, 1]} {self.cell_pos[2, 2]} {self.cell_pos[2, 3]} |
| {self.cell_pos[3, 1]} {self.cell_pos[3, 2]} {self.cell_pos[3, 3]} |
---------""")

    # Changes turn of the players
    def players_turn(self):
        if self.turn == 0:
            self.symbol = 'X'
        elif self.turn == 1:
            self.symbol = 'O'

        self.turn += 1
        if self.turn > 1:
            self.turn = 0

    def players_move(self):
        while True:
            # Outputs the player`s turn
            print(f"Player {self.symbol}'s turn")

            # Writes down in variable coordinates that are typed in console
            self.coordinates = input("PLease, enter the coordinates: ").split()

            # Checking the correctness of input
            commands.conditions()
            answer = commands.conditions()

            # If all requirements are satisfied, then the symbol is staying on the position,
            # according to the entered coordinates and present turn
            if answer is True:
                self.i, self.j = map(int, self.coordinates)
                self.cell_pos[self.i, self.j] = self.symbol
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

        # Returns winning or draw
        if True in win_condition_x:
            return "X wins\n"
        elif True in win_condition_o:
            return "O wins\n"
        elif '_' not in self.cell_pos:
            return "Draw\n"


# Creates the object of class
commands = GameTicTacToe()


# The main algorythm of the game
while True:
    # Outputs game field on the screen
    commands.screen()

    # Switch the players turn
    commands.players_turn()

    # Allows tha player to input his symbol
    commands.players_move()

    # Checks the game conditions
    commands.game()
    result = commands.game()

    # If one of the results is available, turning on the conclusions of the game
    if result == "X wins\n" or result == "O wins\n" or result == "Draw\n":
        # Outputs the final game field and result of the game
        commands.screen()
        print(result)

        # Exit from the game
        break
