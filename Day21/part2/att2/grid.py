import math
class grid:
    def __init__(self, init_string, rule_book):
        self.rule_book = rule_book
        self.grid = [[]]
        for idx, x in enumerate(init_string.split("/")):
            self.grid[0].append(list(x))

    def get_grid(self):
        return self.grid

    def split_grid(self, grid_for_split):
        return_grid = []

        def getsubgrid(x1, y1, x2, y2, sp_grid):
            return [item[x1:x2] for item in sp_grid[y1:y2]]
        if math.sqrt(len(grid_for_split)) % 2 == 0 or len(grid_for_split) == 2:
            split_size = 2
        elif math.sqrt(len(grid_for_split)) % 3 == 0 or len(grid_for_split) == 3:
            split_size = 3
        else:
            raise Exception("Math!")
        i = 0
        while i < len(grid_for_split):
            j =0
            while j < len(grid_for_split[i]):
                return_grid.append(getsubgrid(j,i,j+split_size,i+split_size, grid_for_split))
                j+=split_size
            i+= split_size
        return return_grid

    def get_on_pixels(self):
        count = 0
        for idx, gr in enumerate(self.grid):
            for s_idx, s, in enumerate(gr):
                for c_idx, c in enumerate(s):
                    if c == "#":
                        count += 1
        return count

    def do_grid_split(self):
        build_grid = []
        for idx, gr in enumerate(self.grid):
            split = self.split_grid(gr)
            for s_idx, s_gr in enumerate(split):
                build_grid.append(s_gr)
        self.grid = build_grid

    def do_iteration(self):
        for idx, gr in enumerate(self.grid):
            self.grid[idx] = self.rule_book.get_output(gr)




