from grid_square import grid_square
import math
from enhancement_rule_book import enhancement_rule_book
class program:
    def __init__(self, e_rules, starting_pixels):
        self.rule_book = enhancement_rule_book(e_rules)
        self.pixels = [grid_square(starting_pixels)]

    def get_pixels(self):
        return self.pixels

    def get_on_pixels(self):
        count = 0
        for idx, grid in enumerate(self.pixels):
            count += grid.get_on_pixels()
        return count


    def get_sub_grid(self, grid ,start, size):
        i = start
        sub = []
        while i < start+size:
            j = start
            sub_row = []
            while j < start+size:
                sub_row.append(grid[i][j])
                j+=1
            sub.append(sub_row)
            i+=1
        print("Before split {}".format(grid))
        print("after split {}".format(sub))
        return grid_square(sub)
    def split_grid(self):
        build_grid = []
        for idx, grid in enumerate(self.pixels):
            grid_list = grid.get_grid()
            if math.sqrt(grid.get_grid_length()) % 2 == 0:
                step_size = 2
                jump_len = 4
            elif math.sqrt(grid.get_grid_length()) % 3 == 0:
                step_size = 3
                jump_len = 3
            else:
                raise Exception("Math!")
            i = 0
            
            self.pixels = build_grid

    def do_iteration(self):
        self.split_grid()
        build_grid = []
        for idx, grid in enumerate(self.pixels):
            build_grid.append(self.rule_book.get_grid_transform(grid.get_grid_transformations()))
        #self.pixels = self.rule_book.get_grid_transform(self.pixels.get_grid_transformations())
        self.pixels = build_grid
