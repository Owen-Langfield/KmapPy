from math import log2
from cell import Cell
from utility import *

class KMap: 
    def __init__(self, cell_values):
        if not self.__is_power_of_two(len(cell_values)):
            raise ValueError(f"Number of cells {len(cell_values)} is not valid: must be a power of 2")
        
        self.cell_values = cell_values
        self.number_of_variables = int(log2(len(cell_values)))    

        self.cells = []
        self.SOP_cells = [] 
        'Cells with a value of 1'

        self.__temp_groups = list()
        'Groups found from DFS on one cell, largest one is added to `self.__groups`'
        self.__groups = []
        'The final KMap groups'

        self.__intialise_cells()

    def __is_power_of_two(self, x):
        return x > 0 and (x & (x - 1)) == 0
    
    def __intialise_cells(self):
        SOP_and_DC_cells = [] # Allows us to set the adjacent cells of DC cells, but we do not need to loop through this later, so it is a function variable.

        # Create array using custom Cell class
        # Assuming the array given corrosponds to the array of outputs of a truth table and NOT the graphical KMap position
        for i in range(len(self.cell_values)):
            self.cells.append( Cell(kmap=self, pos=i) )

            if self.cell_values[i] != 0:
                SOP_and_DC_cells.append(self.cells[i])
                if self.cell_values[i] == 1:
                    self.SOP_cells.append(self.cells[i])
        
        # Set adjacent cells for all DC and SOP cells
        for SOPDC_cell in SOP_and_DC_cells:
            bin_pos = int2bin(SOPDC_cell.pos, bit_length=self.number_of_variables) 

            for bit_index in range(len(bin_pos)):
                adj_pos = bin2int(flip_bit(bin_pos, bit_index)) 

                if self.cell_values[adj_pos] != 0:
                    SOPDC_cell.adj.append( self.cells[adj_pos] )

    def solve(self): 
        'Returns a list of prime implicants within the KMap'
        for SOP_cell in self.SOP_cells:
            if SOP_cell.grouped:
                continue
            SOP_cell.find_group([SOP_cell])
            if self.__temp_groups: self.__add_largest_group()
        return self.__groups
    
    def derive_boolean_equations(self, varnames):
        if len(varnames) != self.number_of_variables:
            raise ValueError(f"Number of variable names entered {len(varnames)} is not valid: must be {self.number_of_variables}.")
        boolean_equations = []
        
        for g in range(len(self.__groups)):
            group = self.__groups[g]
            unchanged_cells_pos = 2**(self.number_of_variables)-1
            for i in range(len(group)-1):
                unchanged = ~(group[i].pos ^ group[i+1].pos)
                unchanged_cells_pos = unchanged & unchanged_cells_pos

            unchanged_cells_pos = int2bin(unchanged_cells_pos, self.number_of_variables)
            
            product_term = ""
            for i in range(len(varnames)):
                
                group_term = int2bin(group[0].pos, self.number_of_variables)
                if unchanged_cells_pos[i] == '1':
                    if group_term[i] == '1': product_term += varnames[i]
                    elif group_term[i] == '0': product_term += "~"+varnames[i]
            boolean_equations.append(product_term)     
        return boolean_equations

    # Called by Cells when they find an implicant
    def add_temp_group(self, temp_group):
        self.__temp_groups.append(temp_group)   
        for temp_grouped_cell in temp_group:
            temp_grouped_cell.temp_grouped = True
        
    def __add_largest_group(self):
        MAX_group = self.__temp_groups[0]
        for temp_group in self.__temp_groups:
            for temp_grouped_cell in temp_group:
                temp_grouped_cell.temp_grouped = False
            
            if len(MAX_group) < len(temp_group):
                MAX_group = temp_group
        
        for grouped_cell in MAX_group:
            grouped_cell.grouped = True
        self.__temp_groups.clear()
        
        
        self.__groups.append(MAX_group)
    
    def get_groups(self):
        if not self.__groups: 
            return UserWarning("KMap may not have been solved or no groups where found. Call KMap.solve() prior.")
        return self.__groups
    



            

    