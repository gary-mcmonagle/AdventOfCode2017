get_bin = lambda x: format(x, 'b')

class generator:
    def __init__(self,starting_value, multiply_factor):
        self.current_value = starting_value
        self.multiply_factor = multiply_factor

    def get_next_value(self):
        value = (self.current_value*self.multiply_factor)%2147483647
        self.current_value = value
        return value

    def get_value_as_lowest_binary(self):
        val = get_bin(self.get_next_value())
        while(len(val) < 16):
            val = "0"+val
        if(len(val) > 16):
            val = val[-16:]
        return val

