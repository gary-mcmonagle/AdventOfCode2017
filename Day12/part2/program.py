class program:
    def __init__(self, id, pipes):
        self.id =id
        self.pipes  = pipes

    def get_id(self):
        return self.id
    def get_pipes(self):
        return self.pipes
    def equals(self,program):
        return self.id == program.get_id()

    def __str__(self):
        return "{0}: {1}".format(str(self.id), str(self.pipes))
    def __repr__(self):
        return "{0}: {1}".format(str(self.id),str(self.pipes))