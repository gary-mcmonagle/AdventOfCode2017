class group:
    def __init__(self):
        self.nodes = []
    def add_node(self,grid_square):
        self.nodes.append(grid_square)
    def get_nodes(self):
        return self.nodes