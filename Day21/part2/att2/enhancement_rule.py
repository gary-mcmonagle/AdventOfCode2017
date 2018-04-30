import numpy
class enhancement_rule:
    def __init__(self, input_string, output):
        self.sample_input = []
        for idx, x in enumerate(input_string.split("/")):
            self.sample_input.append(list(x))
        self.output = output
        self.output_grid = []
        for idx, x in enumerate(output.split("/")):
            self.output_grid.append(list(x))

        self.allowed_inputs = [self.sample_input, numpy.flip(self.sample_input,0).tolist(),numpy.flip(self.sample_input,1).tolist() ]
        i = 1
        while i < 4:
            rot = numpy.rot90(self.sample_input, k=i).tolist()
            self.allowed_inputs.append(rot)
            self.allowed_inputs.append(numpy.flip(rot,0).tolist())
            self.allowed_inputs.append(numpy.flip(rot, 1).tolist())
            i+=1
    def get_allowed_inputs(self):
        return self.allowed_inputs
    def does_match(self, test_input):
        for idx, allowed_input in enumerate(self.allowed_inputs):
            if test_input == allowed_input:
                return True
        return False
    def get_output(self):
        return self.output
    def get_output_grid(self):
        return self.output_grid