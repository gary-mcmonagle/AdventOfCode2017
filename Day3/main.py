import csv, os
class MyGrid:
    grid = [[1]]
    sequence = ['R', 'U', 'L', 'D']
    origin = [0,0]
    last_added = [0,0]

    def __init__(self, target):
        self.target = target
        self.add_values(target)
        self.grid.reverse()

    def add_values(self, target):
        line_length = 1
        increase_line_length = False
        direction = 'R'
        y = 0
        i = 2
        while(i <= target):
            count = i
            while (i < (count + line_length)):
                if(i <= target):
                    y = self.get_y_val(y, direction)
                    self.last_added = self.add_value(y, i, direction)
                i+=1
            directionOb = self.get_next_direction(direction,y)
            y = directionOb[1]
            direction = directionOb[0]
            if(increase_line_length):
                line_length = line_length + 1
                increase_line_length = False
            else:
                increase_line_length = True

    def get_next_direction(self, current_direction, y):
        if(current_direction == "R"):
            self.grid.append([])
        if (current_direction == "L"):
            y = y +1
            self.grid.insert(0,[])
            self.origin[1] = self.origin[1]+1
        for index, item in enumerate(self.sequence):
            if(current_direction == item):
                if(index == (len(self.sequence)-1)):
                    return [self.sequence[0],y]
                else:
                    return [self.sequence[index+1],y]

    def add_value(self, y, val, direction):
        self.make_x_adjustments(y,direction)
        if(direction == 'R' or direction == 'U'):
            self.grid[y].append(val)
            xVal = len(self.grid[y])-1
        else:
            self.grid[y].insert(0,val)
            xVal = 0
        return  [xVal, y]

    def make_x_adjustments(self, y, direction):
        if(y == self.origin[1]):
            if(direction == 'L' or direction == 'D'):
                self.origin[0] = self.origin[0]+1

    def get_y_val(self, current_y, direction):
        if(direction == 'U'):
            current_y = current_y + 1
        if(direction == 'D'):
            current_y = current_y - 1
        return current_y

    def __getattr__(self, grid):
        return self.grid

    def  print_grid(self, file_name):
        for index, item in enumerate(self.grid):
            print(item)

    def get_steps(self):
        if(self.last_added[0] > self.origin[0]):
            hor_steps = self.last_added[0] - self.origin[0]
        else:
            hor_steps = self.origin[0] - self.last_added[0]
        if(self.last_added[1] > self.origin[1]):
            ver_steps = self.last_added[1] - self.origin[1]
        else:
            ver_steps = self.origin[1] - self.last_added[1]
        return ver_steps + hor_steps

    def out_csv(self):
        if(os._exists('outputs.csv')):
            os.remove('outputs.csv')
        with open('output.csv', 'w') as myfile:
            self.grid.reverse()
            for index, item in enumerate(self.grid):
                if(len(item) > 0):
                    print(item)
                    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                    wr.writerow(item)

    def __getattr__(self, origin):
            return self.origin
    def __getattr__(self, last_added):
        return self.last_added


gridOb = MyGrid(277678)
#gridOb.out_csv()
print(gridOb.get_steps())










