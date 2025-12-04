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

Below is some pseudocode for how the algorithm works, though it is slightly different to the actual implementation.

```python
groups ← empty list
temp_groups ← empty list
cells ← list of all k-map cells
minterm_cells ← all cells where value = 1

FOR each current_cell IN minterm_cells:
    IF current_cell.grouped = True:
        CONTINUE
    temp_groups ← empty list
    CALL find_group(current_cell, previously_visited = [current_cell])
    ADD largest(temp_groups) TO groups
END FOR

FUNCTION find_group(current_cell, previously_visited):
    FOR each adj_cell IN current_cell.adjacent_cells:
        bit_flip_pos ← the bit position that differs between current_cell and adj_cell
        is_rectangular ← True
        new_cells ← empty list
        FOR each visited_cell IN previously_visited:
            candidate_pos ← flip_bit(visited_cell.pos, bit_flip_pos)
            candidate_cell ← kmap.cells[candidate_pos]
            IF candidate_cell.value = 0:
                is_rectangular ← False
                BREAK
            ELSE:
                ADD candidate_cell TO new_cells
        IF is_rectangular = True:
            all_visited ← previously_visited ∪ new_cells
            CALL find_group(adj_cell, all_visited)
            ADD all_visited TO temp_groups
```

## Status

- Functions as a boolean algebra minmiser using a Karnaugh map inspired algorithm.
- Very little input validation, the program may crash with an incorrect input. 

## Future Work

- A visualiser of the kmap algorithm could be implemented.
- The complete state machine design process could be implemented into the program. State machine diagram -> transiton table -> boolean algebra expression -> final circuit. The 3rd step is complete.
