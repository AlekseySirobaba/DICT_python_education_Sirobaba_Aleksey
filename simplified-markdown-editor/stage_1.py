class MarkdownEditor:

    def __init__(self):
        self.com = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list",
                    "new-line"]

    @staticmethod
    def help():
        return "Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line"


def chcommands():
    while True:
        answer = input("Choose a formatter: > ")
        if answer == "!help":
            print(program.help())
        elif answer == "!done":
            break
        elif answer in program.com:
            pass
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    program = MarkdownEditor()
    chcommands()
