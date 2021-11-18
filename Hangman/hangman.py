import random


class Hangman:

    def __init__(self):
        self.list_of_words = ["python", "java", "javascript", "css", "computer", "console", "keyboard", "sleep"]
        self.guess_letters = list(random.choice(self.list_of_words[0:]))
        self.used_letters = []
        self.players_attempts = 8
        self.screen = {}
        self.answer = ""

    def screen_output(self):

        # Setup the unknown letters
        if self.screen == {}:
            for key, value in enumerate(self.guess_letters):
                self.screen[key] = '-'

        print(self.guess_letters)

        # Output the result on the screen
        print(*self.screen.values(), sep="")
        play.conditions_and_input()

    def conditions_and_input(self):

        # Defeat and win condition
        if self.guess_letters == list(self.screen.values()):
            print("\nYou guessed the word ", *self.screen.values(), "!", "\nYou survived!", sep="")
            print("\nThanks for playing!\nWe'll see how well you did in the next stage!\n")
            play.__init__()
            game_menu()
        elif self.players_attempts <= 0:
            print("\nYou lost!\n")
            play.__init__()
            game_menu()

        # Input the letter
        self.answer = input("Input a letter: ")

        # Checks the length of symbol
        if len(self.answer) == 1:
            # Checks that symbol is actually an English letter and it's register
            if self.answer.isdigit():
                print("Please enter letters")
            else:
                if self.answer.islower() and self.answer.isalpha():
                    play.game()
                else:
                    print("Please enter a lowercase English letter")
        else:
            print("You should input a single letter")

    def game(self):

        if self.answer in self.used_letters:
            print("You've already guessed this letter.")

        elif self.answer in self.guess_letters:

            # Adds new used word to the list
            self.used_letters.append(self.answer)

            # Adds guessed letter to word
            for index, value in enumerate(self.guess_letters):
                if value == self.answer:
                    self.screen[index] = self.answer

        else:
            print("That letter doesn't appear in the word")
            self.players_attempts -= 1
            # Adds new used word to the list
            self.used_letters.append(self.answer)


play = Hangman()


def game_menu():
    menu = input("HANGMAN\nType 'play' to play game,\n'exit' to quit:\n")

    # Outputs the menu on the screen
    while True:
        if menu == 'play':
            play.screen_output()
        elif menu == 'exit':
            break
        else:
            game_menu()


if "__name__" == __name__:
    game_menu()
