from knot import knot
from grid_square import grid_square
from group import group
class disk:

    def __init__(self, grid):
        self.grid = grid
        self.group_count = 0
        self.groups = []

    def add_row_to_grid(self, row):
        self.grid.append(self.convert_hex_to_bin(knot.knot_hash(row)))

    def get_group_count(self):
        return len(self.groups)

    def get_sqaure_by_co_ord(self, y_ax, xax):
        return self.grid[y_ax][xax]

    def create_groups(self):
        for r_idx, row in enumerate(self.grid):
            for s_ind, square in enumerate(row):
                if square.get_is_used() and (not (square.get_has_been_added_to_group())):
                    my_group = group()
                    self.fill_group(square,my_group)
                    self.groups.append(my_group)

    def fill_group(self, start_grid_square,target_group):
        target_group.add_node(start_grid_square)
        nodes_found = True
        while(nodes_found):
            nodes_found = False
            for idx, node in enumerate(target_group.get_nodes()):
                nodes_found = self.add_grid_square_adjacents_to_group(node,target_group)


    def add_grid_square_adjacents_to_group(self, grid_square, target_group):
        any_found = False
        adjacents = [[1,0],[0,1],[0,-1],[-1,0]]
        for idx, ad in enumerate(adjacents):
            y_ax = grid_square.get_co_ord()[0] + ad[0]
            x_ax = grid_square.get_co_ord()[1] + ad[1]
            if x_ax >= 0 and y_ax >=0 and x_ax < 128 and y_ax < 128:
                target_grid = self.get_sqaure_by_co_ord(y_ax, x_ax)
                if target_grid.get_is_used() and (not target_grid.get_has_been_added_to_group()):
                    target_grid.set_added_to_group()
                    target_group.add_node(target_grid)
                    any_found = True
        return any_found

    def convert_binary_to_grid_squares(self):
        for r_idx, row in enumerate(self.grid):
            row_of_grid_squares = []
            for c_idx,char in enumerate(row):
                row_of_grid_squares.append(grid_square(char,r_idx, c_idx))
            self.grid[r_idx] = row_of_grid_squares


    def convert_hex_to_bin(self, input_string):
        return_string = ""
        for idx, char in enumerate(input_string):
            try:
                val = bin(int(char, 16))[2:]
                while (len(val) < 4):
                    val = "0" + val
                return_string += val
            except:
                None
        return return_string

    def get_grid(self):
        return self.grid