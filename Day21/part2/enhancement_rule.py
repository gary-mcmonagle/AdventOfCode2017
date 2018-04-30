from grid_square import grid_square
class enhancement_rule:
    def __init__(self, sample_answer, output):
        self.sample_answer = grid_square(sample_answer)
        self.output = grid_square(output)
        #self.output = output
    def match(self,key):
        return key == self.sample_answer.get_grid()
    def get_output(self):
        return self.output
    def get_sample(self):
        return self.sample_answer
    def __repr__(self):
        return "{} => {}".format(self.sample_answer, self.output)