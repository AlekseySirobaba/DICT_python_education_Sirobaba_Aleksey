class RegularExpressions:
    def __init__(self):
        self.res: bool = False
        self.meta_symbols = ['^', '$']

    def main_alg(self, reg_exp: str) -> bool:
        self.__match_check(reg_exp)
        return self.res

    def __match_check(self, r_e: str):
        split_re = r_e.split('|')
        self.__check_rules(split_re[0].strip(), split_re[1].strip())

    def __check_rules(self, reg_exp: str, text: str, i: int = 0, j: int = 0, correct: list = None) -> bool:
        if correct is None:
            correct = []

        if correct.count(True) == len(reg_exp):
            self.res = True
            return True
        if i == len(text):
            self.res = False
            return False

        m_check = self.__meta_check(reg_exp, text)

        if m_check is None:
            pass
        elif m_check[0].count(True) == m_check[1]:
            self.res = True
            return True
        else:
            return False

        if reg_exp[j] == text[i]:
            correct.append(True)
            self.__check_rules(reg_exp, text, i + 1, j + 1, correct)
        elif reg_exp[j] == '.':
            correct.append(True)
            self.__check_rules(reg_exp, text, i + 1, j + 1, correct)
        elif reg_exp[j] == '' and text[i] != '':
            correct.append(True)
            self.__check_rules(reg_exp, text, i + 1, j + 1, correct)
        elif reg_exp[j] == '' and text[i] == '':
            correct.append(True)
            self.__check_rules(reg_exp, text, i + 1, j + 1, correct)

        elif reg_exp[j] != text[i] and j > 0:
            self.__check_rules(reg_exp, text, i)
        elif (reg_exp[j] != '' and text[i] == '') and j > 0:
            self.__check_rules(reg_exp, text, i)

        elif reg_exp[j] != text[i] and j == 0:
            self.__check_rules(reg_exp, text, i + 1)
        elif (reg_exp[j] != '' and text[i] == '') and j == 0:
            self.__check_rules(reg_exp, text, i + 1)

    def __meta_check(self, reg_ex: str, text: str) -> [list, None]:
        meta_s: list = []
        for syb in reg_ex:
            if syb in self.meta_symbols:
                meta_s.append(syb)

        if meta_s:
            return [self.__meta_symbols(meta_s, reg_ex, text), len(meta_s)]

        return None

    def __meta_symbols(self, meta_s: list, reg_ex: str, text: str) -> list:
        output: list = []
        table_rm: dict = {}.fromkeys(self.meta_symbols, '')
        meta_remove = str.maketrans(table_rm)
        reg_buf = reg_ex = reg_ex.translate(meta_remove)

        if '.' in reg_ex:
            reg_buf = list(reg_buf)

            for key, el in enumerate(reg_buf):
                if el == '.':
                    reg_buf[key] = text[key - 1]

            reg_buf = ''.join(reg_buf)

        if '^' in meta_s:
            output.append(reg_buf == text[:len(reg_ex)])

        if '$' in meta_s:
            output.append(reg_buf == text[len(text) - len(reg_ex):])

        return output


if __name__ == '__main__':
    re = RegularExpressions()
    while True:
        print(f'Output: {re.main_alg(input("Input: "))}')
