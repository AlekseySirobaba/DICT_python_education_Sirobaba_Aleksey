import io
import math
import random


class ArithmeticTest:

    def __init__(self):
        self.acts = ['+', '-', '*']
        self.mark = 0
        self.level_description = ""
        self.all_lvl_on = False

    def levels(self, action):
        if action == '1':
            self.level_description = "level 1 (simple operations with numbers 2-9)"
            atest.test_lvl_1()
        elif action == '2':
            self.level_description = "level 2 (integral squares of 11-29)"
            atest.test_lvl_2()
        elif action == '3':
            self.level_description = "level 3 (square radical of 100-300 [Whole number only, no rounding])"
            atest.test_lvl_3()
        elif action == '4':
            self.level_description = "level 4 (factorial of 4 - 99)"
            atest.test_lvl_4()
        elif action == '5':
            self.level_description = "level 5 (All levels)"
            self.all_lvl_on = True
            atest.all_lvl()
        else:
            print("Please, type number of level you want.")
            return 0

    def input(self):
        while True:
            try:
                answer = int(input('> '))
            except ValueError:
                print("Incorrect answer")
            else:
                return answer

    def test_lvl_1(self):
        res = 0
        for _ in range(5):
            act = random.choice(self.acts)
            a = random.randint(2, 9)
            b = random.randint(2, 9)

            if act == '+':
                res = a + b
            elif act == '-':
                res = a - b
            elif act == '*':
                res = a * b

            print(f"{a} {act} {b}")

            atest.examination(res, atest.input())

    def test_lvl_2(self):
        for _ in range(5):
            a = random.randint(11, 29)

            res = a ** 2

            print(f"{a} ^ 2")

            atest.examination(res, atest.input())

    def test_lvl_3(self):
        for _ in range(5):
            a = random.randint(100, 300)
            res = math.trunc(math.sqrt(a))
            print(f"square radical of {a}")

            atest.examination(res, atest.input())

    def test_lvl_4(self):
        for _ in range(5):
            a = random.randint(3, 10)
            res = 1
            for num in range(1, a + 1):
                res *= num

            print(f"{a}!")

            atest.examination(res, atest.input())

    def all_lvl(self):
        print(f"Level 1")
        atest.test_lvl_1()
        print("-----------\n")

        print(f"Level 2")
        atest.test_lvl_1()
        print("-----------\n")

        print(f"Level 3")
        atest.test_lvl_1()
        print("-----------\n")

        print(f"Level 4")
        atest.test_lvl_1()
        print("-----------\n")

    def examination(self, res, answer):
        if res == answer:
            print("Right!")
            self.mark += 1
        else:
            print("Wrong!")

    def rating(self):
        try:
            rating = open("results.txt", 'r')
        except FileNotFoundError:
            rating = open("results.txt", 'w')

        try:
            text = rating.readlines()
        except io.UnsupportedOperation:
            text = []

        name = input("What is your name?\n")
        if atest.all_lvl_on is True:
            text.append(f"{name}: {self.mark}/20 {self.level_description}\n")
        else:
            text.append(f"{name}: {self.mark}/5 {self.level_description}\n")

        rating_list = open("results.txt", 'w')
        rating_list.writelines(text)
        rating_list.close()
        print('The results are saved in "results.txt".')


def menu():
    while True:
        atest.__init__()
        action = input("""MENU OF ARITHMETIC TEST
1 - To the test
2 - Results list
0 - Exit\n""")

        if action == '0':
            break
        elif action == '1':
            main_alg()
        elif action == '2':
            results_list()
            print()
        else:
            print("Please, type correctly.\n")


def results_list():
    try:
        rating = open("results.txt", 'r')
    except FileNotFoundError:
        print("File is missing: it was deleted or there are no tests passed yet.")
    else:
        text = rating.readlines()
        for line in text:
            print(line.strip('\n'))


def main_alg():
    while True:
        level_choice = atest.levels(input("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
3 - square radical of 100-300 (Whole number only, no rounding)
4 - factorial of 4 - 99
5 - All levels (1-4)\n"""))
        if level_choice == 0:
            pass
        else:
            break

    answers_yes = ["Yes", "YES", "yes", "y"]
    answers_no = ["No", "NO", "no", "n"]
    while True:
        if atest.all_lvl_on is True:
            points = input(f"Your mark is {atest.mark}/20. Would you like to save the result? Enter yes or no.\n")
        else:
            points = input(f"Your mark is {atest.mark}/5. Would you like to save the result? Enter yes or no.\n")

        if points in answers_yes:
            atest.rating()
            break
        elif points in answers_no:
            break
        else:
            print("Please, type correctly.")


if __name__ == "__main__":
    atest = ArithmeticTest()
    menu()
