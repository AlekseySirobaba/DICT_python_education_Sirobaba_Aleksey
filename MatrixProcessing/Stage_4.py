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

        #  Considers the calculates there only one array needed
        if self.action == 2 or self.action == 4:
            self.i, self.j = map(int, input("Enter size of matrix: ").split())
            k = self.i
            z = self.j
            print("Enter matrix:")

        # Input values due to selected array
        else:
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
        for _ in range(len(self.array1)):
            self.array_res.append([])

        # Fills the new matrix with values (each value is sum of elements of two matrix`s)
        for i in range(self.i):
            for j in range(self.j):
                # Considers the type of numbers (int or float)
                if self.array1[i][j].isnumeric() and self.array2[i][j].isnumeric():
                    self.array_res[i].append(int(self.array1[i][j]) + int(self.array2[i][j]))
                else:
                    self.array_res[i].append(round(float(self.array1[i][j]) + float(self.array2[i][j]), 2))

        cmd.result_output()

    def mc_multiply_res(self):
        # Creates list (strings) in the new array according to the size of the first matrix
        for _ in range(len(self.array1)):
            self.array_res.append([])

        # Fills the new matrix with values (each value is multiply of elements of matrix and const)
        for i in range(self.i):
            for j in range(self.j):
                # Considers the type of numbers (int or float)
                if self.array1[i][j].isnumeric():
                    self.array_res[i].append(int(self.array1[i][j]) * int(self.const))
                else:
                    self.array_res[i].append(round(float(self.array1[i][j]) * float(self.const), 2))

        cmd.result_output()

    def mm_multiply_res(self):
        r1 = len(self.array1)  # Number of strings in first matrix
        c1 = len(self.array1[0])  # Number of columns in first matrix
        c2 = len(self.array2[0])  # Number of strings in second matrix
        s = 0
        string = []

        # String of first matrix. Choose n-string of the first matrix
        for z in range(r1):
            #  Column of the second matrix. Choose n-column of the second matrix
            for j in range(c2):
                # Column of first matrix and string of second matrix
                # to calculate chosen first array string and second array column
                for i in range(c1):
                    # Considers the type of numbers (int or float)
                    if self.array1[z][i].isnumeric() and self.array2[i][j].isnumeric():
                        s = s + int(self.array1[z][i]) * int(self.array2[i][j])
                    else:
                        s = s + round(float(self.array1[z][i]) * float(self.array2[i][j]), 2)
                # Input the results of calculating element in string of new array
                string.append(s)
                s = 0
            # Writes down the new string in matrix
            self.array_res.append(string)
            string = []

        cmd.result_output()

    def main_diagonal(self):
        # Creates list (strings) in the new array according to the size of the first matrix
        for _ in range(len(self.array1[0])):
            self.array_res.append([])

        for i in range(len(self.array1[0])):
            for j in range(len(self.array1)):
                self.array_res[i].append(self.array1[j][i])

        cmd.result_output()

    def sub_diagonal(self):
        max_s = len(self.array1) - 1  # Value to start iterating from the last string of matrix

        # Creates list (strings) in the new array according to the size of the first matrix
        for _ in range(len(self.array1[0])):
            self.array_res.append([])
        print(self.array_res)

        for i in range(len(self.array1[0])):
            for j in range(len(self.array1)):
                self.array_res[i].append(self.array1[max_s - j][-1 - i])

        cmd.result_output()

    def vertical(self):
        # Creates list (strings) in the new array according to the size of the first matrix
        for _ in range(len(self.array1[0])):
            self.array_res.append([])

        for i in range(len(self.array1[0])):
            for j in range(len(self.array1)):
                self.array_res[i].append(self.array1[i][-1 - j])

        cmd.result_output()

    def horizontal(self):
        # Creates list (strings) in the new array according to the size of the first matrix
        for _ in range(len(self.array1[0])):
            self.array_res.append([])

        for i in range(len(self.array1[0])):
            for j in range(len(self.array1)):
                self.array_res[i].append(self.array1[-1 - i][j])

        cmd.result_output()

    # Outputs the result on the screen
    def result_output(self):
        string = ""
        print("The result is:")
        for elem in self.array_res:
            for key, pos in enumerate(elem):
                string += str(elem[key]) + " "
            print(string)
            string = ""

        main_menu()


# Algorithm of multiply matrix with constant
def m_by_const():
    cmd.action = 2
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


# Allows choosing type of transposition
def transposition():
    cmd.action = 4
    action = input("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice: """)
    if action == '1':
        cmd.input_array()
        cmd.main_diagonal()
    elif action == '2':
        cmd.input_array()
        cmd.sub_diagonal()
    elif action == '3':
        cmd.input_array()
        cmd.vertical()
    elif action == '4':
        cmd.input_array()
        cmd.horizontal()
    else:
        transposition()


# Allows to choose an option
def main_menu():
    cmd.__init__()  # Resets all values to avoid conflicts of previous calculate
    action = input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
0. Exit
Your choice: """)
    print()
    if action == '1':
        add_matrices()
    elif action == '2':
        m_by_const()
    elif action == '3':
        m_by_matrix()
    elif action == '4':
        transposition()
    elif action == '0':
        pass
    else:
        main_menu()


# Starts the programme from here
if __name__ == "__main__":
    cmd = Matrix()
    main_menu()
