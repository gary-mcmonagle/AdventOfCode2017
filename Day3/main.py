class MyGrid:
    grid = [[1]]
    sequence = ['R', 'U', 'L', 'D']
    origin = [0,0]

    def __init__(self, target):
        self.target = target

    def change_direction(self, current_direction):
        if(current_direction == "R"):
            self.grid.append([])
        if (current_direction == "L"):
            self.grid.insert(0,[])
            self.origin[1]+= 1
        for index, item in enumerate(self.sequence):
            if(current_direction == item):
                if(index == (len(self.sequence)-1)):
                    return self.sequence[0]
                else:
                    return self.sequence[index+1]

    def add_value(self, y, val, append):
        if(append):
            self.grid[y].append(val)
            return
        else:
            self.grid[y].insert(0,val)


    def __getattr__(self, grid):
        return self.grid
    def __getattr__(self, origin):
        return self.origin

gridOb = MyGrid(100)
print(gridOb.origin)
print(gridOb.change_direction('L'))
print(gridOb.grid)
print(gridOb.origin)

