from instructions import instructions
from register import register
class printer:
    def __init__(self, raw_instructions):
        self.execution_instructions=instructions(raw_instructions)
        self.registers = []
        i = 97
        while i < 105:
            self.registers.append(register(chr(i)))
            i += 1
        self.mul_count = 0

    def find_register(self, name):
        for idx, reg in enumerate(self.registers):
            if reg.get_name() == name:
                return reg
        raise Exception("{} register not found".format(name))

    def execute_instruction(self):
        inc_counter = True
        ins = self.execution_instructions.get_instruction()
        if type(ins[2]) is int:
            val = ins[2]
        else:
            val = self.find_register(ins[2]).get_value()
        if ins[0] == "set":
            self.find_register(ins[1]).set_value(val)
        elif ins[0] == "sub":
            current_value = self.find_register(ins[1]).get_value()
            self.find_register(ins[1]).set_value(current_value - val)
        elif ins[0] == "mul":
            current_value = self.find_register(ins[1]).get_value()
            self.find_register(ins[1]).set_value(current_value * val)
            self.mul_count += 1
        elif ins[0] == "jnz":
            if type(ins[1]) is int:
                current_value = ins[1]
            else:
                current_value = self.find_register(ins[1]).get_value()
            if current_value != 0:
                inc_counter = False
                current_value = self.execution_instructions.get_executing_instruction()
                self.execution_instructions.set_executing_instruction(current_value + val)
        else:
            raise Exception("{}".format(ins[0]))
        if inc_counter:
            current_value = self.execution_instructions.get_executing_instruction()
            self.execution_instructions.set_executing_instruction(current_value + 1)

    def run_program(self):
        while(self.execution_instructions.get_executing_instruction() < len(self.execution_instructions.get_instruction_list())):
            #print("In while")
            self.execute_instruction()
        print(self.mul_count)






