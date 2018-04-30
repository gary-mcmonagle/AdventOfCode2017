input.txt
class grid_square:
    def __init__(self, init):
        if type(init) == str:
            self.grid = []
            for idx, x in enumerate(init.split("/")):
                self.grid.append(list(x))
        else: self.grid = init
    def get_grid(self):
        return self.grid
    def get_grid_length(self):
        count = 0
        for idx, row in enumerate(self.grid):
            count += len(row)
        return count

    def get_on_pixels(self):
        count = 0
        for idx, row in enumerate(self.grid):
            for c_idx, c in enumerate(row):
                if(c == "#"):
                    count += 1
        return count

    def get_grid_transformations(self):
        possible_transformations = [self.grid]
        possible_transformations.append(numpy.flip(self.grid, 0).tolist())
        possible_transformations.append(numpy.flip(self.grid, 1).tolist())
        i = 1
        while i < 4:
            rot = numpy.rot90(self.grid, k=i).tolist()
            possible_transformations.append(rot)
            possible_transformations.append(numpy.flip(rot,1).tolist())
            possible_transformations.append(numpy.flip(rot, 0).tolist())
            i+=1
        return possible_transformations
    def __repr__(self):
        return str(self.grid)
    def __str__(self):
        return str(self.grid)



