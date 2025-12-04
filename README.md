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

Below is some pseudocode for how the grouping algorithm works. This returns a list of prime implicants.

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

Once the list of prime implicants have been found, the boolean equations must then be derived. The below pseudocode should describe this:

```python
FUNCTION DeriveBooleanExpressions(groups, variable_names, num_variables):

    boolean_expressions ← empty list

    FOR EACH group IN groups:
        # Step 1: determine which bit positions remain unchanged across all cells in the group
        unchanged_mask ← bitmask with all bits = 1 (size = num_variables)
        FOR i FROM 0 TO (length(group) - 2):
            current_pos  ← group[i].position_bits
            next_pos     ← group[i+1].position_bits
            changed_bits ← XOR(current_pos, next_pos)
            unchanged_bits ← NOT(changed_bits)
            unchanged_mask ← (unchanged_mask AND unchanged_bits)
        unchanged_mask_bits ← convert unchanged_mask TO binary string of length num_variables
        # Step 2: build the product term using only unchanged bits
        reference_pos_bits ← binary representation of group[0].position_bits
        product_term ← empty string
        FOR bit_index FROM 0 TO (num_variables - 1):
            IF unchanged_mask_bits[bit_index] = '1':
                IF reference_pos_bits[bit_index] = '1':
                    product_term ← product_term + variable_names[bit_index]
                ELSE IF reference_pos_bits[bit_index] = '0':
                    product_term ← product_term + "NOT " + variable_names[bit_index]
        APPEND product_term TO boolean_expressions
    RETURN boolean_expressions
```

## Status

- Functions as a boolean algebra minmiser using a Karnaugh map inspired algorithm.
- Very little input validation, the program may crash with an incorrect input. 

## Future Work

- A visualiser of the kmap algorithm could be implemented.
- The complete state machine design process could be implemented into the program. State machine diagram -> transiton table -> boolean algebra expression -> final circuit. The 3rd step is complete.
