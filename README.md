# KmapPy

KmapPy is a simple program that asks the user their variable names and the truth table output as that is dependent on thos variables entered. 

From there it will return prime implicants and the boolean expressions for each one, as well as the final output equation. 

KmapPy was developed for an assigment to avoid solving large kmaps manually. This algorithm *should* work for n-variables, however it has not been tested for more than 6. 

## The algorithm

Once the user has entered their variable names and output column, the algorithm begins. The algorithm is recursive, and finds all possible groupings of a minterm cell and picks the largest.

Defintions:
- A cell is an entry into a kmap and can have a value of 1, 0, or 'X' (dont care).
- Adjacent cell - an adjacent cell is a cell 1 bit flip away from the current cell and has a value of 1 or 'X'.
- Group is short for prime implicant.
- A grouped cell is a cell within a group.
- A minterm is a cell with a value of 1.
- "Flipping a bit" is where we NOT a bit value. (e.g. 1 -> 0, 0 -> 1)

```python
     REPEAT FOR EACH current_cell IN kmap.minterm_cells:
         IF current_cell.grouped == true: CONTINUE TO NEXT ITERATION
         CALL current_cell.find_group()

       FUNCTION find_group(previously_visited_cells):
         SET newly_visited_cells TO EMPTY LIST
         REPEAT FOR EACH adj_cell IN current_cell.adjacent_cells:
             SET bit_flip_position TO *the position of the bit that flipped between current_cell and adj_cell*
             REPEAT FOR EACH prev_cell in previously_visited_cells:
                    # flip_bit returns the bit string with the bit at the specified position flipped
                   SET ungrouped_adjacent_cell_pos TO flip_bit(prev_cell.pos, bit_flip_position)
                 IF kmap.cells[ungrouped_adjacent_cell_pos].value == 0:
                     SET newly_visited_cells TO EMPTY LIST
                     BREAK # not a valid rectangle on the kmap
                 ELSE:
                    APPEND v TO newly_visited_cells
              
11.                
10.       APPEND LARGEST temporary_groups TO groups  # Add largest implicant to list of prime implicants
          SET temp_groups TO EMPTY LIST
11.       REPEAT FOR EACH cell within largest group: cell.grouped = true
```

## Status

- Functions as a boolean algebra minmiser using a Karnaugh map inspired algorithm.
- Very little input validation, the program may crash with an incorrect input. 

## Future Work

- A visualiser of the kmap algorithm could be implemented.
- The complete state machine design process could be implemented into the program. State machine diagram -> transiton table -> boolean algebra expression -> final circuit. The 3rd step is complete.
