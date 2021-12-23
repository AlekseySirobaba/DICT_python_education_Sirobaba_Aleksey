# Introductory words
print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!""")


class CoffeeMachine:

    def __init__(self, action):
        # Records the command, which "the client" typed, into variable
        self.action = action
        # Storage of coffee machine (= cm)
        self.money = 500
        self.amount_of_water = 400
        self.amount_of_milk = 540
        self.amount_of_cb = 120
        self.disposable_cups = 9

    def taking_money(self):

        # Outputs the number of money coffee machine gives
        print("I gave you " + str(self.money) + " hryvnias")

        # Clears "the wallet" of coffee machine
        self.money = 0

    def filling_cm(self):

        # Inputs the number of products to fill
        self.amount_of_water += int(input("Write how many ml of water you want to add:\n"))
        self.amount_of_milk += int(input("Write how many ml of milk you want to add:\n"))
        self.amount_of_cb += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.disposable_cups += int(input("Write how many disposable coffee cups you want to add:\n"))

    def cm_status(self):

        # Checks the status of coffee machine
        print("\nThe coffee machine has:\n" +
              str(self.amount_of_water) + " ml of water\n" +
              str(self.amount_of_milk) + " ml of milk\n" +
              str(self.amount_of_cb) + " grams of coffee beans\n" +
              str(self.disposable_cups) + " of disposable cups\n" +
              str(self.money) + " hryvnias")

    def buying_coffee(self):

        # Setups the recipes of coffee and template to choose one of the coffees
        coffee = dict()
        espresso = dict(water=250, milk=0, cb=16, cost=4)
        latte = dict(water=350, milk=75, cb=20, cost=7)
        cappuccino = dict(water=200, milk=100, cb=12, cost=6)

        # Inputs the type of coffee and opportunity to back to the menu
        answer = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:\n")
        if answer == "back":
            return
        if int(answer) == 1:
            coffee = espresso.copy()
        elif int(answer) == 2:
            coffee = latte.copy()
        elif int(answer) == 3:
            coffee = cappuccino.copy()

        #  Checks if the amount of products is enough
        if self.amount_of_water < coffee.get('water'):
            print("Sorry, not enough water!")
        elif self.amount_of_milk < coffee.get('milk'):
            print("Sorry, not enough milk!")
        elif self.amount_of_cb < coffee.get('cb'):
            print("Sorry, not enough coffee beans!")
        elif self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
        else:

            print("I have enough resources, making you a coffee!")

            # Calculates how many products coffee machine need to produce definite type of coffee
            # and takes it from "storage" of coffee machine, also earns some money
            self.amount_of_water -= coffee.get('water')
            self.amount_of_milk -= coffee.get('milk')
            self.amount_of_cb -= coffee.get('cb')
            self.money += coffee.get('cost')
            self.disposable_cups -= 1


menu = CoffeeMachine(action=" ")

while True:
    menu.action = input("\nWrite action (buy, fill, take, remaining, exit):\n")
    # Gives the opportunity to "the client" to input commands and checks it`s correctness
    if menu.action == "buy":
        menu.buying_coffee()
    elif menu.action == "fill":
        menu.filling_cm()
    elif menu.action == "take":
        menu.taking_money()
    elif menu.action == "remaining":
        menu.cm_status()
    elif menu.action == "exit":
        break
    else:
        print("Please, write commands correctly.")
