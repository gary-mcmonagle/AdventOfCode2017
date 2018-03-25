class packet:
    def __init__(self,delay):
        self.index = -1
        self.caught=False
        self.delay = delay

    def get_index(self):
        return self.index
    def get_caught(self):
        return self.caught
    def get_delay(self):
        return self.delay

    def set_caught(self):
        self.caught = True
    def set_index(self, index):
        self.index = index