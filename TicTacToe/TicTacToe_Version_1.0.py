import numpy as np


class GameTicTacToe:

    def __init__(self):
        self.action = " "
        self.turn = 0
        self.symbol = ' '

        self.coordinates = []
        self.cell_pos = np.full((4, 4), 0, str)

        self.i = 1
        self.j = 1
        for element in range(0, 9):
            self.cell_pos[self.i][self.j] = '_'
            self.j += 1
            if self.j > 3:
                self.i += 1
                self.j = 1

    def main_menu_actions(self):
        while True:
            if self.action == "1":
                commands.player_choosing()
            elif self.action == "2":
                commands.how_to_play()
            elif self.action == "3":
                commands.config()
            break

    def player_choosing(self):
        while True:
            choosing = input("Who will be first? X or O? ----> ")
            if choosing == "X" or choosing == 'O':
                self.symbol = choosing
                if choosing == "X":
                    self.turn = 1
                if choosing == "O":
                    self.turn = 0

                body_of_game()
            else:
                print("Please, choose X or O")

    def how_to_play(self):
        print("""\n       ╔═════════════════════════╗
       ║        TicTacToe        ║
       ║ XXX    THE  GAME    OOO ║    
       ╠═════════════════════════╣
       ║                         ║
       ║  (1, 1)  (1,2)  (1, 3)  ║
       ║                         ║
       ║  (2, 1)  (2,2)  (2, 3)  ║  <------- Coordinates of cells (m, n), there 1 <= m <= 3
       ║                         ║                                              1 <= n <= 3
       ║  (3, 1)  (3,2)  (3, 3)  ║
       ║                         ║ 
       ║  Player's (O or X) turn ║  <------- The player who`s move now
       ╚═════════════════════════╝
PLease, enter the coordinates: 2 3  <------- Type two numbers like this to input the coordinates of cell
                                             and press enter to finish your move\n""")

        while True:
            action = input("To main menu ---> M\n")
            if action == 'M':
                self.action = " "
                break
            else:
                print("Please, press letter 'M' to exit")

    def config(self):
        print("""\nAuthor: Student of 518 group Aleksey Sirobaba
Date v.0.1 creation: 09.12.2021
GitHub: https://github.com/AlekseySirobaba/DICT_python_education_Sirobaba_Aleksey
Email: o.v.sirobaba@student.khai.edu\n""")
        while True:
            action = input("To main menu ---> M\n")
            if action == 'M':
                self.action = " "
                break
            else:
                print("Please, press letter 'M' to exit")

    def screen(self):
        scr = self.cell_pos  # scr = screen
        print(f"""\n       ╔═════════════════════════╗
       ║        TicTacToe        ║
       ║ XXX    THE  GAME    OOO ║    
       ╠═════════════════════════╣
       ║                         ║
       ║       {scr[1, 1]}    {scr[1, 2]}    {scr[1, 3]}       ║
       ║                         ║
       ║       {scr[2, 1]}    {scr[2, 2]}    {scr[2, 3]}       ║
       ║                         ║
       ║       {scr[3, 1]}    {scr[3, 2]}    {scr[3, 3]}       ║
       ║                         ║ 
       ║     Player {self.symbol}'s turn     ║
       ╚═════════════════════════╝""")

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
            commands.screen()
            self.coordinates = input("PLease, enter the coordinates: ").split()

            commands.conditions()
            answer = commands.conditions()

            if answer is not True:
                print(answer)
            if answer is True:
                self.i, self.j = map(int, self.coordinates)
                self.cell_pos[self.i, self.j] = self.symbol
                break

    def conditions(self):
        if not str(self.coordinates[0]).isdigit() or not str(self.coordinates[1]).isdigit():
            return "You should enter numbers!"

        self.i, self.j = map(int, self.coordinates)

        if self.i not in range(1, 4) or self.j not in range(1, 4):
            return "Coordinates should be from 1 to 3."
        elif self.cell_pos[self.i, self.j] != '_':
            return "This cell is occupied! Choose another one!"
        else:
            return True

    def game(self):
        win_condition_x = []
        win_condition_o = []

        for counter in range(1, 4):

            values_h = (self.cell_pos[counter, 1:].tolist())
            values_v = (self.cell_pos[1:, counter].tolist())

            win_condition_x.append(bool(values_h == ['X', 'X', 'X'] or values_v == ['X', 'X', 'X']))
            win_condition_o.append(bool(values_h == ['O', 'O', 'O'] or values_v == ['O', 'O', 'O']))

        d_1 = [self.cell_pos[1, 1], self.cell_pos[2, 2], self.cell_pos[3, 3]]
        d_2 = [self.cell_pos[3, 1], self.cell_pos[2, 2], self.cell_pos[1, 3]]

        win_condition_x.append(d_1 == ['X', 'X', 'X'] or d_2 == ['X', 'X', 'X'])
        win_condition_o.append(d_1 == ['O', 'O', 'O'] or d_2 == ['O', 'O', 'O'])

        if True in win_condition_x:
            return "X wins"
        elif True in win_condition_o:
            return "O wins"
        elif '_' not in self.cell_pos:
            return " Draw "


def body_of_game():
    while True:
        commands.players_move()
        commands.players_turn()
        commands.game()
        result = commands.game()

        if result == "X wins" or result == "O wins" or result == " Draw ":
            scr = commands.cell_pos  # scr = screen
            print(f"""\n       ╔═════════════════════════╗
       ║        TicTacToe        ║
       ║ XXX    THE  GAME    OOO ║    
       ╠═════════════════════════╣
       ║                         ║
       ║       {scr[1, 1]}    {scr[1, 2]}    {scr[1, 3]}       ║
       ║                         ║
       ║       {scr[2, 1]}    {scr[2, 2]}    {scr[2, 3]}       ║
       ║                         ║
       ║       {scr[3, 1]}    {scr[3, 2]}    {scr[3, 3]}       ║
       ║                         ║ 
       ║          {result}         ║
       ╚═════════════════════════╝""")
            commands.__init__()
            print("")
            main_menu()


def main_menu():
    while True:
        print(f"""       ╔═════════════════════════╗
       ║        TicTacToe        ║
       ║ XXX    THE  GAME    OOO ║    
       ╠═════════════════════════╣
       ║  1. Play                ║
       ║  (player selection)     ║
       ║  2. How to play         ║
       ║  3. Configurations      ║
       ║  4. Exit                ║ 
       ║                   v.1.0 ║
       ╚═════════════════════════╝""")

        commands.action = input("Choose the option you need from 1 to 4: ")
        if commands.action == "1" or commands.action == "2" or commands.action == "3":
            commands.main_menu_actions()
        elif commands.action == "4":
            break
        else:
            print("Please, choose from 1 to 4")


if __name__ == "__main__":
    commands = GameTicTacToe()
    main_menu()
