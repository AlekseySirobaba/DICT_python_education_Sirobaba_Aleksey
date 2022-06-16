class RegularExpressions:
    def __init__(self):
        self.res: bool = False  # Need to have these value, because output from recursive method __check_rules is None.

    def main_alg(self, reg_exp: str) -> bool:
        self.__match_check(reg_exp)
        return self.res

    def __match_check(self, r_e: str):
        split_re = r_e.split('|')
        self.__check_rules(split_re[0].strip(), split_re[1].strip())

    def __check_rules(self, reg_exp: str, word: str, i: int = 0, j: int = 0, correct: list = None) -> bool:
        if correct is None:
            correct = []

        if correct.count(True) == len(reg_exp):
            self.res = True
            return True
        if i == len(word):
            self.res = False
            return False

        if reg_exp[j] == word[i]:
            correct.append(True)
            self.__check_rules(reg_exp, word, i + 1, j + 1, correct)
        elif reg_exp[j] == '.':
            correct.append(True)
            self.__check_rules(reg_exp, word, i + 1, j + 1, correct)
        elif reg_exp[j] == '' and word[i] != '':
            correct.append(True)
            self.__check_rules(reg_exp, word, i + 1, j + 1, correct)
        elif reg_exp[j] == '' and word[i] == '':
            correct.append(True)
            self.__check_rules(reg_exp, word, i + 1, j + 1, correct)

        elif reg_exp[j] != word[i] and j > 0:
            self.__check_rules(reg_exp, word, i)
        elif (reg_exp[j] != '' and word[i] == '') and j > 0:
            self.__check_rules(reg_exp, word, i)

        elif reg_exp[j] != word[i] and j == 0:
            self.__check_rules(reg_exp, word, i + 1)
        elif (reg_exp[j] != '' and word[i] == '') and j == 0:
            self.__check_rules(reg_exp, word, i + 1)


if __name__ == '__main__':
    re = RegularExpressions()
    while True:
        print(f'Output: {re.main_alg(input("Input: "))}')
