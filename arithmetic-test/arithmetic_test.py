# ========= Stage 1 =========

import random

acts = ['+', '-', '*']

act = random.choice(acts)
a = random.randint(2, 9)
b = random.randint(2, 9)
res = 0

print(f"{a} {act} {b}")

answer = int(input('> '))

if act == '+':
    res = a + b
elif act == '-':
    res = a - b
elif act == '*':
    res = a * b

if res == answer:
    print("Right!")
else:
    print("Wrong!")
