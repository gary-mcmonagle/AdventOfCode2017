class computing_cluster:
    def __init__(self, con_list):
        self.cluster = con_list
        self.current_node = [12, 12]
        self.direction = 0
        self.infected_count = 0

    def grow_grid(self):
        clean_row = []
        for idx, node in enumerate(self.cluster[0]):
            clean_row.append(".")
        self.cluster.append(clean_row.copy())
        self.cluster.insert(0, clean_row.copy())
        for idx, row in enumerate(self.cluster):
            self.cluster[idx].append(".")
            self.cluster[idx].insert(0, ".")
        self.current_node[0] += 1
        self.current_node[1] += 1
    def get_cluster(self):
        return self.cluster

    def change_direction(self, was_infected):
        if(was_infected):
            self.direction+=1
        else:
            self.direction-=1
        if(self.direction == 4):
            self.direction = 0
        if(self.direction == -1):
            self.direction = 3

    def move_current_node(self):
        grown = False
        if(self.current_node[0] == 0 or self.current_node[1] == 0):
            self.grow_grid()
            grown = True
        if(self.current_node[1] == len(self.cluster)-1 or self.current_node[0] == len(self.cluster)-1):
            if(not grown):
                self.grow_grid()
        if(self.direction == 0):
            self.current_node[0] -= 1
        if(self.direction == 2):
            self.current_node[0] += 1
        if(self.direction == 1):
            self.current_node[1] += 1
        if (self.direction == 3):
            self.current_node[1] -= 1

    def get_infected_count(self):
        return self.infected_count

    def do_burst(self):
        #print(self.cluster[self.current_node[0]][self.current_node[1]])
        #print(self.direction)
        node_infected = self.cluster[self.current_node[0]][self.current_node[1]] == "#"
        self.change_direction(node_infected)
        #print(self.direction)
        if(node_infected):
            self.cluster[self.current_node[0]][self.current_node[1]] = "."
        else:
            self.infected_count += 1
            self.cluster[self.current_node[0]][self.current_node[1]] = "#"
        self.move_current_node()






