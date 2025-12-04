from utility import *
class Cell:
    def __init__(self, kmap, pos, adj = None):
        self.kmap = kmap
        self.pos = pos
        self.adj = [] if adj is None else adj
        self.bin_pos = int2bin(pos, kmap.number_of_variables)

        self.visited_cells = [] 
        'List of cells within rectangle. \n\nPrevents DFS from moving to cells within group'

        self.temp_grouped = False
        self.grouped = False

    def __eq__(self, other):
        return self.kmap == other.kmap and self.pos == other.pos

    def __repr__(self):
        return f"{self.pos}"

    def __is_valid_rectangle(self, visited_cells, bit_flip_pos, new_visited):
        is_rect = True
        
        for v in range(len(visited_cells)):
            adjacent_cell_bin_pos = flip_bit(visited_cells[v].bin_pos, bit_flip_pos)
            adjacent_cell_index = bin2int( adjacent_cell_bin_pos )

            if self.kmap.cell_values[adjacent_cell_index] == 0:
                new_visited.clear()
                is_rect = False
                break

            new_visited.append(self.kmap.cells[adjacent_cell_index])
            
        return is_rect


    def find_group(self, visited_cells=None):
        visited_cells = [] if visited_cells is None else visited_cells
        # If no adjacent cells, add group of self
        if not self.adj:
            self.kmap.add_temp_group([self])
        # If there are adjacent cells:
        # 1. Check the bit flip change and apply it to all previousl visited cells
        for adj_cell in self.adj:
            if adj_cell in visited_cells:
                continue
            
            new_visited = []

            # Get the positon of the bit that flips
            bin_change = int2bin(self.pos ^ adj_cell.pos, self.kmap.number_of_variables)
            bit_flip_pos = bin_change.index("1")

            # Apply the bit flip to all previously visited cells
            # If the rectangle is valid, add it to temp_groups and repeat for the next cell (adj_cell)
            if self.__is_valid_rectangle(visited_cells, bit_flip_pos, new_visited):
                group = visited_cells.copy()
                group.extend(new_visited)
                self.kmap.add_temp_group(group)

                passed_visited = group
                adj_cell.find_group(passed_visited)
            