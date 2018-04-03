class grid:
    def __init__(self):
        self.nodes = [[1]]
        self.origin = [0,0]
        #R0 U1 L2 D3
        self.direction = 0
        self.current_location = [0,0]
        self.line_length = 1
        self.line_counter = 0
        self.line_repeated = 0
        self.is_first = True

    def get_nodes(self):
        return self.nodes

    def get_origin(self):
        return self.origin

    def add_value(self, value):
        self.line_counter += 1
        if (self.direction == 0):
            self.move_right(value)
        if (self.direction == 1):
            self.move_up(value)
        if (self.direction == 2):
            self.move_left(value)
        if (self.direction == 3):
            self.move_down(value)
        self.last_location = self.current_location
        if(self.line_counter == self.line_length):
            self.change_direction()

    def change_direction(self):
        print("Changing Direction")
        self.line_counter = 0
        self.line_repeated += 1
        if(self.line_repeated == 2):
            self.line_length += 1
            self.line_repeated = 0
        self.direction += 1
        if(self.direction == 4):
            self.direction = 0
        self.validate_grid()
        print("Direction = {}".format(self.direction))

    def validate_grid(self):
        if(self.direction == 1):
            blank_list = []
            for idx, node in enumerate(self.nodes[len(self.nodes)-1]):
                blank_list.append(None)
            self.nodes.append(blank_list)
        if(self.direction == 3):
            blank_list = []
            for idx, node in enumerate(self.nodes[0]):
                blank_list.append(None)
            self.nodes.insert(0,blank_list)
            self.current_location[0]+=1
            self.origin[0]+=1



    def move_right(self,value):
        self.current_location[1] += 1
        print("Current location = {}".format(self.current_location))
        if(len(self.nodes[self.current_location[0]]) == self.current_location[1]):
            self.nodes[self.current_location[0]].append(None)
        self.nodes[self.current_location[0]][self.current_location[1]] = value

    def insert_left_column(self):
        for idx, row in enumerate(self.nodes):
            row.insert(0,None)
        self.origin[1] += 1

    def get_distance(self):
        return abs(self.last_location[0] - self.origin[0]) + abs(self.last_location[1] - self.origin[1])

    def move_left(self,value):
        self.current_location[1] -= 1
        if(self.current_location[1] == -1):
            self.insert_left_column()
            self.current_location[1]+=1
        print("Current location = {}".format(self.current_location))
        self.nodes[self.current_location[0]][self.current_location[1]] = value

    def move_up(self,value):
        self.current_location[0] += 1
        print("Current location = {}".format(self.current_location))
        try:
            self.nodes[self.current_location[0]][self.current_location[1]] = value
        except:
            self.nodes[self.current_location[0]].append(value)


    def move_down(self,value):
        self.current_location[0] -= 1
        print("Current location = {}".format(self.current_location))
        self.nodes[self.current_location[0]][self.current_location[1]] = value




