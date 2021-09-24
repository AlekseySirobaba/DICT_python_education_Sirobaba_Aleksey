print("Hello! My name is Speaker_Bot.\nI was created in 2021 by Aleksey Sirobaba")
print("Please, remind me your name")
name = input()
print("What a great name you have, " + name)
print("Let me guess your age.\nEnter remainders of dividing your age by 3, 5, 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is " + str(age) + "; that`s a good time to start programming!")
print("Now I will prove to you that I can count any number you want.")
counting_number = int(input())
for a in range(1, counting_number + 1):
    print(str(a) + " !")