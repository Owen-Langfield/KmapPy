# KmapPy

KmapPy is a simple program that asks the user their variable names and the truth table output as that is dependent on thos variables entered. 

From there it will return prime implicants and the boolean expressions for each one, as well as the final output equation. 

KmapPy was developed for an assigment to avoid solving large kmaps manually. This algorithm *should* work for n-variables, however it has not been tested for more than 6. 

## The algorithm

Once the user has entered their variable names and output column, the algorithm begins. The algorithm is recursive, and finds all possible groupings of a minterm cell and picks the largest.

Defintions:
- Adjacent cell: an adjacent cell is a cell 1 bit flip away from the current cell and has a value of 1 or 'X' (dont care).
- group is short for prime implicant.
- A grouped cell is one within a group.

'''
1. REPEAT until all minterm cells are grouped
2.   Pick an ungrouped minterm cell - where cell.grouped = false
3.     REPEAT for each adjacent cell
4.       Move to one of its adjacent cells
5.       Find the bit that had to flip to get to that adjacent cell.
6.       Apply the bit change to all previously visited cells.
7.       IF one of the previously visited cells move to a cell with 0,
8.         cancel and check next adjacent cell
9.       OTHERWISE add the list of visited cells to temp_groups[]
10.   Add the largest of temp_groups[] to groups[]
11.   FOR each cell within largest group, cell.grouped = true
'''

## Status

- Functions as a boolean algebra minmiser using a Karnaugh map inspired algorithm.
- Very little input validation, the program may crash with an incorrect input. 

## Future Work

- A visualiser of the kmap algorithm could be implemented.
- The complete state machine design process could be implemented into the program. State machine diagram -> transiton table -> boolean algebra expression -> final circuit. The 3rd step is complete.
