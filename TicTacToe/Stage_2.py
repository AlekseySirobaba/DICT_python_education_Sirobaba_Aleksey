# Inputs the symbols in dictionary with key index
cell_pos = dict(enumerate(input("Enter cells: ")))

# Outputs the gaming field with values from cell_pos in exact positions
print("""---------
| """ + str(cell_pos[0]) + " " + str(cell_pos[1]) + " " + str(cell_pos[2]) + """ |
| """ + str(cell_pos[3]) + " " + str(cell_pos[4]) + " " + str(cell_pos[5]) + """ |
| """ + str(cell_pos[6]) + " " + str(cell_pos[7]) + " " + str(cell_pos[8]) + """ |
---------""")
