class Matrix:

    def __init__(self):
        self.array1 = []
        self.array2 = []
        self.array_res = []
        self.a = self.array1
        self.const = 0

    # Switches to the next array to add some values
    def array_switch(self):
        if self.a == self.array1:
            self.a = self.array2
        else:
            self.a = self.array1

    # Creates matrix from empty list and fills it with values
    def input_array(self):
        # Sets the size of matrix (characteristics of array)
        self.a.append(input(">>> ").split())

        # According to amount of strings, fills each of x-number of lists with input values
        for i in range(int(self.a[0][0])):
            while True:
                self.a.append(input(">>> ").split())

                # Checks the correctness of input
                if len(self.a[i + 1]) == int(self.a[0][1]):
                    break
                else:
                    self.a.pop()
                    if int(self.a[0][1]) == 1:
                        print(f"It should be {self.a[0][1]} column")
                    else:
                        print(f"It should be {self.a[0][1]} columns")

    # Inputs the const value
    def input_const(self):
        self.const = int(input())

    # Outputs two created matrix with mathematical sign "+" between them
    def array_output(self):
        string = ""

        # Checks each list (string of matrix) of matrix1 and outputs it`s values on the screen
        for elem in self.a:
            for key, pos in enumerate(elem):
                string += elem[key] + " "
            print(string)
            string = ""

    # Checks the possibility of addition of two matrices
    def conditions(self):
        # Condition, that checks the equality of first lists (strings) of matrix, which have matrix size in it
        # If sizes are equal then proceeds calculating
        if self.array1[0] == self.array2[0]:
            cmd.m_add_result()
        else:
            print("ERROR")

    def m_add_result(self):
        # Creates list (strings) in the new array according to the size of the first matrix
        # - 1, because it doesn't need to consider first list with matrix size
        for _ in range(len(self.array1) - 1):
            self.array_res.append([])

        # Fills the new matrix with values (each value is sum of elements of two matrix`s)
        for i in range(int(self.array1[0][0])):
            for j in range(int(self.array1[0][1])):
                self.array_res[i].append(int(self.array1[i + 1][j]) + int(self.array2[i + 1][j]))

        # Outputs the result on the screen
        string = ""
        for elem in self.array_res:
            for key, pos in enumerate(elem):
                string += str(elem[key]) + " "
            print(string)
            string = ""

    def mc_multiply_res(self):
        # Creates list (strings) in the new array according to the size of the first matrix
        # - 1, because it doesn't need to consider first list with matrix size
        for _ in range(len(self.array1) - 1):
            self.array_res.append([])

        # Fills the new matrix with values (each value is multiply of elements of matrix and const)
        for i in range(int(self.array1[0][0])):
            for j in range(int(self.array1[0][1])):
                self.array_res[i].append(int(self.array1[i + 1][j]) * self.const)

        # Outputs the result on the screen
        string = ""
        for elem in self.array_res:
            for key, pos in enumerate(elem):
                string += str(elem[key]) + " "
            print(string)
            string = ""


# Algorithm of multiply matrix with constant
def m_by_const():
    print("Array:")
    cmd.input_array()  # Inputs the values for the array
    print("Constant:")
    cmd.input_const()  # Inputs const number

    cmd.array_output()  # Outputs array
    print("*")
    print(cmd.const)  # Outputs const number
    print("=")
    cmd.mc_multiply_res()  # Outputs the results of calculating


# Algorithm of adding matrices
def add_matrices():
    print("For first array")
    cmd.input_array()  # Inputs the values for the first array
    cmd.array_switch()  # Switches to the next array
    print("For second array")
    cmd.input_array()  # Inputs the values for the second array

    cmd.array_output()  # Outputs the first array with "+"
    print("+")
    cmd.array_switch()  # Switches to the next array
    cmd.array_output()  # Outputs the second array
    print("=")
    cmd.conditions()  # Checks the possibility of calculating. If true then calls the method to calculate and output
    # In other situations -- returns error


# Allows to choose an option
def main_menu():
    action = input("""1. Add matrices
2. Multiply matrix by a constant
0. Exit\n""")
    if action == '1':
        add_matrices()
    elif action == '2':
        m_by_const()
    elif action == '0':
        pass
    else:
        main_menu()


# Starts the programme from here
if __name__ == "__main__":
    cmd = Matrix()
    main_menu()
