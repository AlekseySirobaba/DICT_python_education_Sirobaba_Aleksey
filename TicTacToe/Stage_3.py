class GameTicTacToe:

    # Set up the positions of symbols
    def __init__(self, cell_pos):
        self.cell_pos = cell_pos

    def screen(self):
        #  Output the symbols on the gaming field
        print(
            f"""            ---------
            | {self.cell_pos[0]} {self.cell_pos[1]} {self.cell_pos[2]} |
            | {self.cell_pos[3]} {self.cell_pos[4]} {self.cell_pos[5]} |
            | {self.cell_pos[6]} {self.cell_pos[7]} {self.cell_pos[8]} |
            ---------""")

    def conditions(self):
        # Values that counts (h) horizontal and (v) vertical combinations
        counter_h = 0
        counter_v = 0

        # Values that counts the number of X and O on playing field
        counter_x = 0
        counter_o = 0

        # Lists which contains bool values about if there are 3 'X' or 3 'O' combinations
        win_condition_x = []
        win_condition_o = []

        while counter_h <= 6 and counter_v <= 2:

            # These block of commands read the columns and lines of gaming field and writes the result in the list
            values_h = []  # h - horizontal
            values_v = []  # v - vertical
            for key in (counter_h, counter_h + 1, counter_h + 2):
                values_h.append(self.cell_pos[key])
            for key in (counter_v, counter_v + 3, counter_v + 6):
                values_v.append(self.cell_pos[key])

            # Checks the data on 3 "X" or "3" "O" combinations and writes down the result
            win_condition_x.append(bool(values_h == ['X', 'X', 'X'] or values_v == ['X', 'X', 'X']))
            win_condition_o.append(bool(values_h == ['O', 'O', 'O'] or values_v == ['O', 'O', 'O']))

            # Counts the number of X and O on gaming field
            if counter_x == 0 or counter_o == 0:
                for symbol in self.cell_pos.values():
                    if symbol == 'X':
                        counter_x += 1
                    if symbol == 'O':
                        counter_o += 1

            # Goes to the next lines and columns
            counter_h += 3
            counter_v += 1

        # Returns winning or other game status
        if abs(counter_x - counter_o) >= 2 or True in win_condition_o and True in win_condition_x:
            return "\nImpossible"
        elif True in win_condition_x:
            return "\nX wins"
        elif True in win_condition_o:
            return "\nO wins"
        elif "_" in self.cell_pos.values():
            return "\nGame not finished"
        else:
            return "\nDraw"


# Body of the game
while True:
    # Creates an object of class and inputs the positions of symbols
    commands = GameTicTacToe(dict(enumerate(input("Enter cells: "))))

    commands.screen()  # Calls method that shows the gaming field

    commands.conditions()  # Calls method that checks the gaming field status

    # Outputs the result of the game
    result = commands.conditions()
    print(result)
