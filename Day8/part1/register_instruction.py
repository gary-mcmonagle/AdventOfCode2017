class register_instruction:
    def __init__(self, register, direction, amount, condition):
        self.register = register
        self.direction = direction
        self.amount = amount
        self.condition = condition

    def get_register(self):
        return self.register
    def set_register(self, register):
        self.register = register

    def get_direction(self):
        return self.direction
    def set_direction(self, direction):
        self.direction = direction

    def get_amount(self):
        return self.amount
    def set_amount(self, amount):
        self.amount = amount

    def get_condition(self):
        return self.condition
    def set_condition(self, condition):
        self.condition = condition