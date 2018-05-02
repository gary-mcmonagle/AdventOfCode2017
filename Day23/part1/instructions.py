class instructions:
    def __init__(self, raw_instructions):
        self.executing_instruction = 0
        self.executing_instructions = []
        for idx, i in enumerate(raw_instructions):
            ins = i.split(" ")[0]
            try:
                targ = int(i.split(" ")[1])
            except:
                targ = i.split(" ")[1]
            try:
                val = int(i.split(" ")[2])
            except:
                val = i.split(" ")[2]
            self.executing_instructions.append([ins,targ,val])

    def get_instruction(self):
        return self.executing_instructions[self.executing_instruction]
    def get_executing_instruction(self):
        return self.executing_instruction
    def set_executing_instruction(self, val):
        self.executing_instruction = val
    def get_instruction_list(self):
        return self.executing_instructions


