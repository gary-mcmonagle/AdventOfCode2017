class layer:

    scanner_index = 0
    scanner_direction = 'D'

    def __init__(self, data):
        self.depth = data[0]
        if(len(data) == 2):
            self.layer_range = data[1]
        else:
            self.layer_range = None

    def get_depth(self):
        return self.depth

    def get_layer_range(self):
        return self.layer_range

    def get_scanner_index(self):
        if(self.layer_range == None):
            return None
        else:
            return self.scanner_index

    def move_scanner_down(self):
        self.scanner_index += 1
        if(self.scanner_index == self.layer_range-1):
            self.scanner_direction = 'U'

    def move_scanner_up(self):
        self.scanner_index -= 1
        if(self.scanner_index == 0):
            self.scanner_direction = 'D'

    def move_snanner(self):
        if(not self.layer_range == None):
            if(self.scanner_direction == 'U'):
                self.move_scanner_up()
            else:
                self.move_scanner_down()


