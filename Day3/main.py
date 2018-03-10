class MyGrid:
    grid = [[1]]
    sequence = ['R', 'U', 'L', 'D']

    def __init__(self, target):
        self.target = target
        self.add_values(target)

    def add_values(self, target):
        line_length = 1
        increase_line_length = False
        direction = 'R'
        y = 0
        i = 2
        while(i < target):
            count = i
            while (i < (count + line_length)):
                y = self.get_y_val(y, direction)
                self.add_value(y, i, direction)
                i+=1
            directionOb = self.get_next_direction(direction,y)
            y = directionOb[1]
            direction = directionOb[0]
            if(increase_line_length):
                line_length = line_length + 1
                increase_line_length = False
            else:
                increase_line_length = True

    def add_values_in_direction(self, count, direction, line_length, y):
        i = count
        while(i <= (count+line_length)):
            y = self.get_y_val(y, direction)
            self.add_value(y, i, direction)
            i = i+1
        return y

    def get_next_direction(self, current_direction, y):
        if(current_direction == "R"):
            self.grid.append([])
        if (current_direction == "L"):
            y = y +1
            self.grid.insert(0,[])
        for index, item in enumerate(self.sequence):
            if(current_direction == item):
                if(index == (len(self.sequence)-1)):
                    return [self.sequence[0],y]
                else:
                    return [self.sequence[index+1],y]

    def add_value(self, y, val, direction):
        xVal = None
        if(direction == 'R' or direction == 'U'):
            self.grid[y].append(val)
            xVal = len(self.grid[y])-1
        else:
            self.grid[y].insert(0,val)
            xVal = 0
        return  [xVal, y]


    def get_y_val(self, current_y, direction):
        if(direction == 'U'):
            current_y = current_y + 1
        if(direction == 'D'):
            current_y = current_y - 1
        return current_y

    def __getattr__(self, grid):
        return self.grid


    def printGrid(self):
        for index, item in enumerate(self.grid):
            print(item)
gridOb = MyGrid(35)
print(gridOb.printGrid())



