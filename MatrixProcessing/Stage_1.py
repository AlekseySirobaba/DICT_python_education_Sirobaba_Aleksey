class Matrix:

    def __init__(self):
        self.array1 = []
        self.array2 = []
        self.a = self.array1

    # Switches to the next array to add some values
    def array_switch(self):
        self.a = self.array2

    # Creates matrix from empty list and fills it with values
    def input_array(self):
        # Sets the size of matrix (characteristics of array)
        self.a.append(input(">>> ").split())

        # According to amount of strings, fills each of x-number of lists with input values
        for i in range(int(self.a[0][0])):
            self.a.append(input(">>> ").split())

    # Outputs two created matrix with mathematical sign "+" between them
    def arrays_output(self):
        string = ""

        # Checks each list (string of matrix) of matrix1 and outputs it`s values on the screen
        for elem in self.array1:
            for key, pos in enumerate(elem):
                string += elem[key] + " "
            print(string)
            string = ""

        print("+")

        # Checks each list (string of matrix) of matrix2 and outputs it`s values on the screen
        for elem in self.array2:
            for key, pos in enumerate(elem):
                string += elem[key] + " "
            print(string)
            string = ""

    # Checks the possibility of addition of two matrices
    def conditions(self):
        print("=")

        # Condition, that checks the equality of first lists (strings) of matrix, which have matrix size in it
        # If sizes are equal then proceeds calculating
        if self.array1[0] == self.array2[0]:
            cmd.result()
        else:
            print("ERROR")

    def result(self):
        array_res = []

        # Creates list (strings) in the new array according to the size of the first matrix
        # - 1, because it doesn't need to consider first list with matrix size
        for _ in range(len(self.array1) - 1):
            array_res.append([])

        # Fills the new matrix with values (each value is sum of elements of two matrix`s)
        for i in range(int(self.array1[0][0])):
            for j in range(int(self.array1[0][1])):
                array_res[i].append(int(self.array1[i + 1][j]) + int(self.array2[i + 1][j]))

        # Outputs the result on the screen
        string = ""
        for elem in array_res:
            for key, pos in enumerate(elem):
                string += str(elem[key]) + " "
            print(string)
            string = ""


# Main algorithm of methods
def main_body():

    print("For first array")
    cmd.input_array()  # Inputs the values for the first array

    cmd.array_switch()  # Switches to the next array

    print("For second array")
    cmd.input_array()  # Inputs the values for the second array

    cmd.arrays_output()  # Outputs the two arrays with "+" between them

    cmd.conditions()  # Checks the possibility of calculating. If true then calls the method to calculate and output
    # In other situations -- returns error


# Starts the programme from here
if __name__ == "__main__":
    cmd = Matrix()
    main_body()
