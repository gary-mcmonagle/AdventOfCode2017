from enhancement_rule import enhancement_rule
class program:
    def __init__(self, rules, pixels):
        self.rules = enhancement_rule(rules)
        self.pixels = pixels
    def do_iteration(self):
        if len(self.pixels) % 9 == 0:
            step_size = 3
        elif len(self.pixels) % 16 == 0:
            step_size = 2
        else:
            raise Exception("Bad length")
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
        print(build_string)

    def get_pixels(self):
        return self.pixels



