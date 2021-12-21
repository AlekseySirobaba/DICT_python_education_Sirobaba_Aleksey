class Matrix:

    def __init__(self):
        self.array1 = []
        self.array2 = []
        self.array_res = []
        self.a = self.array1
        self.const = 0
        self.action = 0
        self.j = 0
        self.i = 0
        self.m = 0
        self.n = 0

    # Switches to the next array to add some values
    def array_switch(self):
        if self.a == self.array1:
            self.a = self.array2
        else:
            self.a = self.array1

    # Creates matrix from empty list and fills it with values
    def input_array(self):

        # Sets the size of matrix (characteristics of array)
        if self.a == self.array1:
            self.i, self.j = map(int, input("Enter size of first matrix: ").split())
            k = self.i
            z = self.j
            print("Enter first matrix:")
        else:
            self.m, self.n = map(int, input("Enter size of second matrix: ").split())
            k = self.m
            z = self.n
            print("Enter second matrix:")

        # According to amount of strings, fills each of x-number of lists with input values
        for i in range(k):
            while True:
                self.a.append(input("> ").split())

                # Checks the correctness of input
                if len(self.a[i]) == z:
                    break
                else:
                    self.a.pop()
                    if int(z) == 1:
                        print(f"It should be {z} column")
                    else:
                        print(f"It should be {z} columns")

    # Inputs the const value
    def input_const(self):
        self.const = input("Enter constant: ")

    # Checks the possibility of action between two matrices
    def conditions(self):
        if [self.i, self.j] == [self.m, self.n] and self.action == 1:
            cmd.m_add_result()
        elif len(self.array1) == len(self.array2[0]) and self.action == 3:
            cmd.mm_multiply_res()
        else:
            print("The operation cannot be performed.")
            main_menu()

    def m_add_result(self):
        # Creates list (strings) in the new array according to the size of the first matrix
        # - 1, because it doesn't need to consider first list with matrix size
        for _ in range(len(self.array1)):
            self.array_res.append([])

        # Fills the new matrix with values (each value is sum of elements of two matrix`s)
        for i in range(self.i):
            for j in range(self.j):
                if self.array1[i][j].isnumeric() and self.array2[i][j].isnumeric():
                    self.array_res[i].append(int(self.array1[i][j]) + int(self.array2[i][j]))
                else:
                    self.array_res[i].append(round(float(self.array1[i][j]) + float(self.array2[i][j]), 2))

        # Outputs the result on the screen
        print("The result is:")
        string = ""
        for elem in self.array_res:
            for key, pos in enumerate(elem):
                string += str(elem[key]) + " "
            print(string)
            string = ""

        main_menu()

    def mc_multiply_res(self):
        # Creates list (strings) in the new array according to the size of the first matrix
        # - 1, because it doesn't need to consider first list with matrix size
        for _ in range(len(self.array1)):
            self.array_res.append([])

        # Fills the new matrix with values (each value is multiply of elements of matrix and const)
        for i in range(self.i):
            for j in range(self.j):
                if self.array1[i][j].isnumeric():
                    self.array_res[i].append(int(self.array1[i][j]) * int(self.const))
                else:
                    self.array_res[i].append(round(float(self.array1[i][j]) * float(self.const), 2))

        # Outputs the result on the screen
        print("The result is:")
        string = ""
        for elem in self.array_res:
            for key, pos in enumerate(elem):
                string += str(elem[key]) + " "
            print(string)
            string = ""

        main_menu()

    def mm_multiply_res(self):
        r1 = len(self.array1)  # Number of strings in first matrix
        c1 = len(self.array1[0])  # Number of columns in first matrix
        c2 = len(self.array2[0])  # Number of strings in second matrix
        s = 0
        string = []

        # String of first matrix
        for z in range(0, r1):
            #  Column of the second matrix
            for j in range(0, c2):
                for i in range(0, c1):
                    if self.array1[z][i].isnumeric() and self.array2[i][j].isnumeric():
                        s = s + int(self.array1[z][i]) * int(self.array2[i][j])
                    else:
                        s = s + round(float(self.array1[z][i]) * float(self.array2[i][j]), 2)
                string.append(s)
                s = 0
            self.array_res.append(string)
            string = []

        # Outputs the result on the screen
        print("The result is:")
        string = ""
        for elem in self.array_res:
            for key, pos in enumerate(elem):
                string += str(elem[key]) + " "
            print(string)
            string = ""

        main_menu()


# Algorithm of multiply matrix with constant
def m_by_const():
    cmd.input_array()
    cmd.input_const()
    cmd.mc_multiply_res()


# Algorithm of multiply matrices
def m_by_matrix():
    cmd.action = 3
    cmd.input_array()
    cmd.array_switch()
    cmd.input_array()
    cmd.conditions()


# Algorithm of adding matrices
def add_matrices():
    cmd.action = 1
    cmd.input_array()
    cmd.array_switch()
    cmd.input_array()
    cmd.conditions()


# Allows to choose an option
def main_menu():
    cmd.__init__()  # Resets all values to avoid conflicts of previous calculate
    action = input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: """)
    if action == '1':
        add_matrices()
    elif action == '2':
        m_by_const()
    elif action == '3':
        m_by_matrix()
    elif action == '0':
        pass
    else:
        main_menu()


# Starts the programme from here
if __name__ == "__main__":
    cmd = Matrix()
    main_menu()
