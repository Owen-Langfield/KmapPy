from utility import *
from kmap import KMap

def parse_array_input(arr):
    arr = arr.removeprefix("[")
    arr = arr.removesuffix("]")
    arr = arr.replace(" ", "")
    arr = arr.replace('"', "")
    arr = arr.replace("'", "")
    arr = arr.split(",")

    return arr
# Q3, Q2, Q1, Q0, On, Dc 
print("## KMAP SOLVER ##\n")
print("Welcome to KMAP SOLVER!\n" )
print("Enter ESC to escape the program\n")
print("Your input should be an array of outputs from your truth table: [0, 'X', 1, 0, ...].\n" \
"The order of the array should be from the first to the last entry in the truth table.\n" \
"---------------------------------------------------------------------------------------")

#Q3,Q2,Q1,Q0
running = True
var_names = parse_array_input(input("\nPlease enter your variable names for this session:\n"))

while running:
    int_cells = parse_array_input(input("\nPlease enter the truth table output column as an array:\n", ))
    if int_cells == "ESC": running = False; 

    for i in range(len(int_cells)):
        if int_cells[i] == "1": 
            int_cells[i] = 1
        elif int_cells[i] == "0": 
            int_cells[i] = 0

    kmap = KMap(int_cells)
    Sop = kmap.SOP_cells

    # [print(i.pos) for i in Sop]
    # [[print(Sop[i].pos, Sop[i].adj[x].pos) for x in range(len(Sop[i].adj))] for i in range(len(Sop))]

    groups = kmap.solve()
    boolean_equations = kmap.derive_boolean_equations(var_names)
    print("PRIME IMPLICANTS FOUND")
    [print(g) for g in groups]
    print("PRODUCT TERMS")
    [print(be) for be in boolean_equations]
    print("OUTPUT EQUATION")

    final_equation = [be+" + " for be in boolean_equations]
    final_equation = ''.join(final_equation)
    final_equation = final_equation.removesuffix(" + ")

    [print(final_equation)]









