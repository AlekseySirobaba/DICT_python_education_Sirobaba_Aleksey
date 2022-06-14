class FormattersMdE:

    @staticmethod
    def newline():
        return ""

    @staticmethod
    def plain(txt):
        return txt

    @staticmethod
    def bold(txt):
        return f"**{txt}**"

    @staticmethod
    def italic(txt):
        return f"*{txt}*"

    @staticmethod
    def inline_code(txt):
        return f"`{txt}`"

    @staticmethod
    def link(label, link):
        return f"[{label}]({link})"

    @staticmethod
    def header(num, txt):
        return "#" * num + txt

    @staticmethod
    def lvl_check(num):
        try:
            int(num)
        except ValueError:
            return 0
        else:
            num = int(num)
            if num < 1 or num > 6:
                return 0

    @staticmethod
    def ordered_list(num, *args):
        ord_list = []
        for line_num in range(num):
            ord_list.append(f"{line_num + 1}. {args[line_num]}")
        return ord_list

    @staticmethod
    def unordered_list(num, *args):
        un_ord_list = []
        for line_num in range(num):
            un_ord_list.append(f"* {args[line_num]}")
        return un_ord_list

    @staticmethod
    def rows_check(num):
        try:
            int(num)
        except ValueError:
            return 0
        else:
            num = int(num)
            if num < 1 or num > 10:
                return 0


class MarkdownEditor(FormattersMdE):

    def __init__(self):
        self.com = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list",
                    "new-line"]
        self.txt_lines = []

    @staticmethod
    def help():
        return """Available formatters: plain bold italic header link inline-code 
                ordered-list unordered-list new-line

Available commands: !help !done !change-line !create-line"""

    @staticmethod
    def format_choose(action):

        if action == "new-line":
            return program.newline()

        elif action == "plain":
            return program.plain(input("Text: "))

        elif action == "bold":
            return program.bold(input("Text:  "))

        elif action == "italic":
            return program.italic(input("Text:  "))

        elif action == "inline-code":
            return program.inline_code(input("Text:  "))

        elif action == "link":
            return program.link(input("Label:  "), input("Link:  "))

        elif action == "header":
            while True:
                lvl = input("Level:  ")
                if program.lvl_check(lvl) == 0:
                    print("Please, type the level number from 1 to 6")
                else:
                    return program.header(int(lvl), input("Text:  "))

        elif action == "ordered-list" or action == "unordered-list":
            while True:
                rows_num = input("Number of rows:  ")
                if program.rows_check(rows_num) == 0:
                    print("Please, type the rows number from 1 to 10")
                else:
                    text = []
                    rows_num = int(rows_num)
                    for num in range(rows_num):
                        text.append(input(f"Row#{num + 1}: "))
                    break

            if action == "ordered-list":
                return program.ordered_list(rows_num, *text)
            else:
                return program.unordered_list(rows_num, *text)

    def create_line(self):
        while True:
            formatter = program.format_input(input("Please, choose formatter: "))

            if formatter == 0:
                print("Please, type format correctly")
            else:
                result = program.format_choose(formatter)
                if isinstance(result, list) is True:
                    return self.txt_lines.extend(result)
                else:
                    return self.txt_lines.append(result)

    def change_line(self):
        delete_text = False
        line = program.line_choose()

        while True:
            formatter = program.format_input(input("Please, choose formatter: "))

            if formatter == 0:
                print("Please, type format correctly")
            else:
                result = program.format_choose(formatter)
                if self.txt_lines[line] != "":
                    delete_text = program.txt_delete()
                return program.changing_process(line, result, delete_text)

    def line_choose(self):
        for num, line in enumerate(self.txt_lines):
            print(num + 1, line, sep=':   ')

        while True:
            try:
                num_line = int(input("Type number of the line which you want to change\n"))
            except ValueError:
                print("Please, type numbers")
            else:
                if num_line < 1 or num_line > len(self.txt_lines):
                    print("Please, choose the number correctly")
                else:
                    break

        return num_line - 1

    @staticmethod
    def txt_delete():
        while True:
            try:
                option = int(input("Do you want to delete the existed text?\n1.Yes\n2.No\n"))
            except ValueError:
                print("Please, type number")
            else:
                if option not in [1, 2]:
                    print("Please, type '1' (Yes) or '2' (No)")
                else:
                    break

        if option == 1:
            return True
        else:
            return False

    def changing_process(self, line, txt, delete):
        if delete is True:
            if isinstance(txt, list) is True:
                for num, text in enumerate(txt):
                    self.txt_lines.insert(line + num, text)
                self.txt_lines.pop(line + len(txt))

        else:
            if isinstance(txt, list) is True:
                self.txt_lines[line] = f"{self.txt_lines[line]} {txt[0]}"
                for num, text in enumerate(txt[1:]):
                    self.txt_lines.insert(line + 1 + num, text)

            else:
                self.txt_lines[line] = f"{self.txt_lines[line]} {txt}"

        return self.txt_lines

    def format_input(self, formatter):
        if formatter not in self.com:
            return 0
        else:
            return formatter

    def text_viewer(self):
        for line in self.txt_lines:
            print(line)

    def save_output(self):
        text = open("output.md", 'w')
        for line in self.txt_lines:
            text.write(line + '\n')
        text.close()


def commands():
    while True:
        answer = input("Choose a command: > ")
        if answer == "!help":
            print(program.help())
        elif answer == "!done":
            program.save_output()
            break
        elif answer == "!create-line":
            program.create_line()
            program.text_viewer()
        elif answer == "!change-line":
            program.change_line()
            program.text_viewer()
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    program = MarkdownEditor()
    commands()
