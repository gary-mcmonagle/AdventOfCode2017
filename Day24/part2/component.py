class component:
    def __init__(self, a_type, b_type):
        self.a_type = a_type
        self.b_type = b_type
        self.is_connected = False
        self.value = a_type + b_type

    def does_match(self, port_type):
        if port_type == self.a_type:
            return self.b_type
        if port_type == self.b_type:
            return self.a_type
        return False

    def set_connected(self):
        self.is_connected = True

    def get_connected(self):
        return self.is_connected

    def get_value(self):
        return self.value
