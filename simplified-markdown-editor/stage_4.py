class MarkdownEditor:

    def __init__(self):
        self.com = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list",
                    "new-line"]
        self.txt_lines = []

    @staticmethod
    def help():
        return "Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line"

    def text_editor(self, action):
        if action == "plain":
            self.txt_lines.append(input("Text: "))

        elif action == "bold":
            self.txt_lines.append(f"**{input('Text: > ')}**")

        elif action == "italic":
            self.txt_lines.append(f"*{input('Text: > ')}*")

        elif action == "header":
            while True:
                try:
                    level = int(input("Level: > "))
                except ValueError:
                    print("Please, type only number")
                else:
                    if level < 1 or level > 6:
                        print("Please, type a number from 1 to 6")
                    else:
                        break

            self.txt_lines.append(f"#" * level + f"{input('Text: > ')}")

        elif action == "link":
            self.txt_lines.append(f"[{input('Label: > ')}]({input('URL: > ')})")

        elif action == "inline-code":
            self.txt_lines.append(f"`{input('Text: > ')}`")

        elif action == "new-line":
            self.txt_lines.append("")

        elif action == "ordered-list":
            rows_num = program.rows_num()
            for num in range(1, rows_num + 1):
                self.txt_lines.append(f"{num}. {input(f'Row #{num}: > ')}")

        elif action == "unordered-list":
            rows_num = program.rows_num()
            for num in range(1, rows_num + 1):
                self.txt_lines.append(f"* {input(f'Row #{num}: > ')}")

        return self.txt_lines

    @staticmethod
    def rows_num():
        while True:
            try:
                num = int(input("Number of rows: > "))
            except ValueError:
                print("Please, type only number")
            else:
                if num < 1:
                    print("The number of rows should be greater than zero")
                else:
                    return num

    @staticmethod
    def text_viewer(txt):
        for line in txt:
            print(line)

    def save_output(self):
        text = open("output.md", 'w')
        for line in self.txt_lines:
            text.write(line + '\n')
        text.close()


def chcommands():
    while True:
        answer = input("Choose a formatter: > ")
        if answer == "!help":
            print(program.help())
        elif answer == "!done":
            program.save_output()
            break
        elif answer in program.com:
            program.text_viewer(program.text_editor(answer))
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    program = MarkdownEditor()
    chcommands()
