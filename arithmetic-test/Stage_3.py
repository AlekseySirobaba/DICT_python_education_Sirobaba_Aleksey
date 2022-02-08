import io
import random


class ArithmeticTest:

    def __init__(self):
        self.acts = ['+', '-', '*']
        self.mark = 0
        self.level_description = ""

    def levels(self, action):
        if action == '1':
            self.level_description = "level 1 (simple operations with numbers 2-9)"
            for _ in range(5):
                atest.test_lvl_1()
        elif action == '2':
            self.level_description = "level 2 (integral squares of 11-29)"
            for _ in range(5):
                atest.test_lvl_2()
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
        a = random.randint(11, 29)

        res = a ** 2

        print(f"{a}")

        atest.examination(res, atest.input())

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
        text.append(f"{name}: {self.mark}/5 {self.level_description}\n")

        rating_list = open("results.txt", 'w')
        rating_list.writelines(text)
        rating_list.close()
        print('The results are saved in "results.txt".')


def main_alg():
    atest.__init__()
    while True:
        level_choice = atest.levels(input("""Which level do you want? Enter a number:
    1 - simple operations with numbers 2-9
    2 - integral squares of 11-29\n"""))
        if level_choice == 0:
            pass
        else:
            break

    answers_yes = ["Yes", "YES", "yes", "y"]
    answers_no = ["No", "NO", "no", "n"]
    while True:
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
    main_alg()
