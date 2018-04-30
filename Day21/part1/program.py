import math
from enhancement_rule import enhancement_rule

class program:
    def __init__(self, rules, pixels):
        self.rules = enhancement_rule(rules)
        self.pixels = pixels
        self.step_size = 2
    def do_iteration(self):
        if(math.sqrt(len(self.pixels)) % 3 == 0):
            step_size = 3
        elif (math.sqrt(len(self.pixels)) % 2 == 0):
            step_size = 2
        else:
            raise Exception("Math")

        i = 0
        build_string = ""
        while i < len(self.pixels):
            print("START {}".format(i))
            print("END {}".format(i+step_size*step_size))
            print(self.pixels[i:i+step_size*step_size])
            print(self.rules.get_out_pattern(self.pixels[i:i+step_size*step_size]))
            build_string += self.rules.get_out_pattern(self.pixels[i:i+step_size*step_size])
            #print(build_string)
            i+=step_size*step_size
        self.pixels = build_string
        if(step_size == 2):
            self.step_size = 3
        if(step_size == 3):
            self.step_size = 2
        print(build_string)

    def get_pixels(self):
        return self.pixels



