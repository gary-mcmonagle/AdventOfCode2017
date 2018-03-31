class register:
    def __init__(self,letter):
        self.letter = letter
        self.value = 0

    def get_letter(self):
        return self.letter
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value

    def __str__(self):
        return "Letter:{0} Value:{1}".format(self.letter,self.value)