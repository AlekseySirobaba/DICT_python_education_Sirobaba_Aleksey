class RegularExpressions:
    def __init__(self):
        self.__res: bool = False
        self.__meta_symbols = ['^', '$', '?', '*', '+', '\\', '.']

    def main_alg(self, reg_exp: str) -> bool:
        self.__match_check(reg_exp)
        return self.__res

    def __match_check(self, r_e: str):
        split_re = r_e.split('|')
        self.__check_rules(split_re[0].strip(), split_re[1].strip())

    def __check_rules(self, reg_exp: str, text: str, i: int = 0, j: int = 0, correct: list = None,
                      metas: bool = None) -> bool:

        if correct is None:
            correct = []

        if correct.count(True) == len(reg_exp):
            self.__res = True
            return True
        if i == len(text):
            self.__res = False
            return False

        if metas is False:
            pass
        else:
            m_check = self.__meta_check(reg_exp, text)

            if m_check is None or m_check is not None and m_check[0] == []:
                metas = False
                reg_exp = m_check[2]
            elif m_check[0].count(True) == m_check[1]:
                self.__res = True
                return True
            else:
                return False



        if reg_exp[j] == text[i]:
            correct.append(True)
            self.__check_rules(reg_exp, text, i + 1, j + 1, correct, metas)
        elif reg_exp[j] == '.':
            correct.append(True)
            self.__check_rules(reg_exp, text, i + 1, j + 1, correct, metas)
        elif reg_exp[j] == '' and text[i] != '':
            correct.append(True)
            self.__check_rules(reg_exp, text, i + 1, j + 1, correct, metas)
        elif reg_exp[j] == '' and text[i] == '':
            correct.append(True)
            self.__check_rules(reg_exp, text, i + 1, j + 1, correct, metas)

        elif reg_exp[j] != text[i] and j > 0:
            self.__check_rules(reg_exp, text, i, metas=metas)
        elif (reg_exp[j] != '' and text[i] == '') and j > 0:
            self.__check_rules(reg_exp, text, i, metas=metas)

        elif reg_exp[j] != text[i] and j == 0:
            self.__check_rules(reg_exp, text, i + 1, metas=metas)
        elif (reg_exp[j] != '' and text[i] == '') and j == 0:
            self.__check_rules(reg_exp, text, i + 1, metas=metas)

    def __meta_check(self, reg_ex: str, text: str) -> [list, None]:
        meta_s: list = []
        for key, syb in enumerate(reg_ex):
            if syb in self.__meta_symbols and reg_ex[key - 1]:
                meta_s.append(syb)

        if meta_s:
            return self.__meta_proc(meta_s, reg_ex, text)

        return None

    @staticmethod
    def __meta_proc(meta_s: list, reg_ex: str, text: str) -> list:
        output: list = []
        table_rm: dict = {'$': '', '^': ''}
        meta_remove = str.maketrans(table_rm)
        reg_buf = reg_ex = reg_ex.translate(meta_remove)

        if '\\' in reg_ex and '\\' in meta_s:
            for key, el in enumerate(reg_buf):
                if el == "\\":
                    meta_s.remove(reg_buf[key + 1])
                    meta_s.remove(el)
                    reg_buf = list(reg_buf)
                    reg_buf.remove(el)
                    reg_buf = ''.join(reg_buf)
                    break

        elif "." in reg_ex and "." in meta_s:
            reg_buf = list(reg_buf)

            for key, el in enumerate(reg_buf):
                if el == '.':
                    reg_buf[key] = text[key - 1]

            reg_buf = ''.join(reg_buf)

        if '?' in meta_s:
            match = 0
            for key, el in enumerate(reg_buf):
                if el == '?':
                    sym = reg_buf[key - 1]
                    for val in text[key - 1:]:
                        if sym == val:
                            match += 1

            if match in range(0, 2):
                output.append(True)
            else:
                output.append(False)

        if '*' in meta_s:
            match = 0
            for key, el in enumerate(reg_buf):
                if el == '*':
                    sym = reg_buf[key - 1]
                    slice_s = text[key - 1:]
                    i = 0
                    while sym == slice_s[i]:
                        if sym == slice_s[i]:
                            match += 1
                        i += 1

            if match >= 0:
                output.append(True)
            else:
                output.append(False)

        if '+' in meta_s:
            match = 0
            for key, el in enumerate(reg_buf):
                if el == '*':
                    sym = reg_buf[key - 1]
                    slice_s = text[key - 1:]
                    i = 0
                    while sym == slice_s[i]:
                        if sym == slice_s[i]:
                            match += 1
                        i += 1

            if match > 0:
                output.append(True)
            else:
                output.append(False)

        if '^' in meta_s:
            output.append(reg_buf == text[:len(reg_buf)])

        if '$' in meta_s:
            output.append(reg_buf == text[-len(reg_buf):])

        return [output, len(meta_s), reg_buf]


if __name__ == '__main__':
    re = RegularExpressions()
    while True:
        print(f'Output: {re.main_alg(input("Input: "))}')
