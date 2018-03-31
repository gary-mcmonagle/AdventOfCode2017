from register import register
class tablet:
    def __init__(self, instructions):
        self.instructions = instructions
        self.registers = []
        self.last_played_sound = None
        self.executing_instruction = 0


    def validate_register_exists(self,target_register):
        for idx, tablet_register in enumerate(self.registers):
            if(tablet_register.get_letter() == target_register):
                return
        self.registers.append(register(target_register))

    def execute_instrutions(self):
        while(self.executing_instruction <len(self.instructions)):
            instruction = self.instructions[self.executing_instruction]
            self.execute_instruction(instruction[0],instruction[1],instruction[2])
    def get_target_value(self, target_value):
        if(target_value == None):
            return target_value
        elif(isinstance(target_value,int)):
            return target_value
        else:
            return self.get_regiter(target_value).get_value()

    def execute_instruction(self, action, target_register, target_value):
        increment_count = True
        self.validate_register_exists(target_register)
        target_value = self.get_target_value(target_value)
        if(action == "set"):
            self.get_regiter(target_register).set_value(target_value)
        if (action == "add"):
            self.get_regiter(target_register).set_value(self.get_regiter(target_register).get_value() + target_value)
        if (action == "mul"):
            self.get_regiter(target_register).set_value(self.get_regiter(target_register).get_value() * target_value)
        if (action == "mod"):
            self.get_regiter(target_register).set_value(self.get_regiter(target_register).get_value() % target_value)
        if(action == "snd"):
            self.last_played_sound = self.get_regiter(target_register).get_value()
        if(action == "jgz"):
            if(self.get_regiter(target_register).get_value() > 0):
                increment_count = False
                self.executing_instruction += target_value
        if(action == "rcv"):
            if (self.get_regiter(target_register).get_value() > 0):
                print("Value = {}".format(self.last_played_sound))
                exit()
        if(increment_count):
            self.executing_instruction += 1

    def get_registers(self):
        return self.registers
    def get_regiter(self,name):
        for idx, tablet_register in enumerate(self.registers):
            if(tablet_register.get_letter() == name):
                return tablet_register
        raise Exception("{} not found".format(name))
