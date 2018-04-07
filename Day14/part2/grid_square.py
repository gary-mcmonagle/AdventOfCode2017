class grid_square:
    def __init__(self, bin_value,y_ind, x_ind):
        self.is_used = bin_value == "1"
        self.has_been_visited = False
        self.co_ord = [y_ind,x_ind]
        self.has_been_added_to_group = False

    def set_added_to_group(self):
        self.has_been_added_to_group = True
    def get_has_been_added_to_group(self):
        return self.has_been_added_to_group

    def set_visited(self):
        self.has_been_visited = True

    def get_co_ord(self):
        return self.co_ord


    def get_has_been_visted(self):
        return self.has_been_visited
    def get_is_used(self):
        return self.is_used

