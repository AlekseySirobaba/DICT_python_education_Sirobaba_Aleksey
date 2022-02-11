import random

acts = ['+', '-', '*']
res = 0
mark = 0
for _ in range(5):
    act = random.choice(acts)
    a = random.randint(2, 9)
    b = random.randint(2, 9)

    print(f"{a} {act} {b}")

    while True:
        try:
            answer = int(input('> '))
        except ValueError:
            print("Incorrect answer")
        else:
            break

    if act == '+':
        res = a + b
    elif act == '-':
        res = a - b
    elif act == '*':
        res = a * b

    if res == answer:
        print("Right!")
        mark += 1
    else:
        print("Wrong!")

print(f"Your mark is {mark}/5")
