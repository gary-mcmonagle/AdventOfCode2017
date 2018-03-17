import json
from register_instruction import register_instruction
from register import register
class cpu_registers:
    def __init__(self):
        self.instructions = []
        for idx, ins in enumerate(json.load(open('input.json'))):
            self.instructions.append(register_instruction(ins[0],ins[1],int(ins[2]),[ins[4],ins[5],int(ins[6])]))
        self.register_set_up()

    def register_set_up(self):
        self.registers = []
        for idx, ins in enumerate(self.instructions):
            found = False
            for reg_idx,reg in enumerate(self.registers):
                if(reg.get_name() == ins.get_register()):
                    found = True
            if(not found):
                self.registers.append(register(ins.get_register()))

    def get_instructions(self):
        return self.instructions
    def get_registers(self):
        return self.registers

    def find_register(self,name):
        for idx, reg in enumerate(self.registers):
            if(reg.get_name() == name):
                return reg
        return None

    def evaluate_condition(self, condition):
        quereied_register = self.find_register(condition[0])
        if(condition[1] == "=="):
            return quereied_register.get_value() == condition[2]
        elif(condition[1] == "!="):
            return not quereied_register.get_value() == condition[2]
        elif (condition[1] == ">"):
            return quereied_register.get_value() > condition[2]
        elif (condition[1] == "<"):
            return quereied_register.get_value() < condition[2]
        elif (condition[1] == "<="):
            return quereied_register.get_value() <= condition[2]
        elif (condition[1] == ">="):
            return quereied_register.get_value() >= condition[2]
        else:
            raise Exception('This is the exception you expect to handle')

    def execute_instruction(self, instruction):
        if(self.evaluate_condition(instruction.get_condition())):
            if(instruction.get_direction() == "inc"):
                self.find_register(instruction.get_register()).set_value(self.find_register(instruction.get_register()).get_value() + instruction.get_amount())
            if(instruction.get_direction() == "dec"):
                self.find_register(instruction.get_register()).set_value(self.find_register(instruction.get_register()).get_value() - instruction.get_amount())

    def execute_conditions(self):
        for idx, ins in enumerate(self.instructions):
            self.execute_instruction(ins)
    def get_largest_registery(self):
        largest_value = self.registers[0].get_value()
        print(largest_value)
        for idx, reg in enumerate(self.registers):
            if((reg.get_value()) > largest_value):
                largest_value = reg.get_value()
        return largest_value







