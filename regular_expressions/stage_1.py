class RegularExpressions:
    def main_alg(self, reg_exp: str) -> bool:
        if self.__match_check(reg_exp):
            return True
        return False

    @staticmethod
    def __match_check(r_e: str) -> bool:
        strip_re = r_e.split('|')
        if strip_re[0] == strip_re[1]:
            return True
        elif strip_re[0] == '.':
            return True
        elif strip_re[0] == '' and strip_re[1] != '':
            return True
        elif strip_re[0] == '' and strip_re[1] == '':
            return True
        elif strip_re[0] != '' and strip_re[1] == '':
            return False


if __name__ == '__main__':
    re = RegularExpressions()
    print(f'Output: {re.main_alg(input("Input: "))}')
