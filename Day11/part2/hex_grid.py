class hex_grid:
    move_rules = {
        "n":[[-1,0],[-1,0]],
        "s":[[1,0],[1,0]],
        "ne":[[-1,1],[0,1]],
        "nw":[[-1,-1],[0,-1]],
        "se":[[0,1],[1,1]],
        "sw":[[0,-1],[1,-1]]
    }
    opposite_moves = {
        "n":"s",
        "s":"n",
        "ne":"sw",
        "sw":"ne",
        "se":"nw",
        "nw":"se"
    }
    largest_distance = 0
    def __init__(self, moves):
        self.co_ord = [0,0]
        for idx, move in enumerate(moves):
            self.move(move)
    def move(self,direction):
        odd_index = 0
        if(not self.co_ord[1] % 2 ==0):
            odd_index = 1
        self.co_ord[0] += self.move_rules[direction][odd_index][0]
        self.co_ord[1] += self.move_rules[direction][odd_index][1]
        if(self.get_distance() > self.largest_distance):
            self.largest_distance = self.get_distance()

    def get_largest_distance(self):
        return self.largest_distance

    def get_distance(self):
        diag = self.get_diagonal(self.get_direction(self.co_ord), self.get_co_ord())
        return abs(self.co_ord[0] - diag[0][0]) + diag[1]



    def get_diagonal(self, direction, intersection):
        count = 0
        co_orrid = [0,0]
        stil_valid = True
        while(True):
            if(co_orrid[0] == intersection[0] or co_orrid[1] == intersection[1]):
                return [co_orrid,count]
            odd_index = 0
            if(not count % 2 == 0):
                odd_index = 1
            co_orrid[0] += self.move_rules[direction][odd_index][0]
            co_orrid[1] += self.move_rules[direction][odd_index][1]
            count += 1

    def get_direction(self,co_ord):
        direction = ""
        if(co_ord[0] >= 0):
            direction += "s"
        else:
            direction += "n"
        if(co_ord[1] >= 0):
            direction += "e"
        else:
            direction += "w"
        return direction




    def get_co_ord(self):
        return self.co_ord

