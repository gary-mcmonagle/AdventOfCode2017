class register:
    def __init__(self, name):
        self.value = 0
        self.name = name
        if(name == "a"):
            self.value = 1

    def get_value(self):
        return self.value
    def set_value(self, new_value):
        self.value = new_value
    def get_name(self):
        return self.name
