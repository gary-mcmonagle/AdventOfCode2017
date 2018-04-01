from register import register
class program:
    def __init__(self, instructions,id):
        self.instructions = instructions
        self.executing_instruction = 0
        self.queue = []
        self.registers=[]
        self.registers.append(register("p"))
        self.registers[0].set_value(id)
        self.sent_count = 0
        self.is_waiting = False
        self.is_terminated = False
        self.id = id

    def get_regiter(self,name):
        for idx, tablet_register in enumerate(self.registers):
            if(tablet_register.get_letter() == name):
                return tablet_register
        raise Exception("{} not found".format(name))

    def get_target_value(self, target_value):
        if(target_value == None):
            return target_value
        elif(isinstance(target_value,int)):
            return target_value
        else:
            return self.get_regiter(target_value).get_value()

    def ensure_register(self,target_register):
        try:
            int(target_register)
            return
        except:
            self.registers.append(register(target_register))

    def execute_instruction(self, pair_program):
        increment_count = True
        if(self.executing_instruction >= len(self.instructions) or self.executing_instruction < 0):
            self.is_terminated = True
        if(not self.is_terminated):
            if(not self.is_waiting):
                action = self.instructions[self.executing_instruction][0]
                target_register = self.instructions[self.executing_instruction][1]
                self.ensure_register(target_register)
                target_value = self.get_target_value(self.instructions[self.executing_instruction][2])
                if (action == "set"):
                    self.get_regiter(target_register).set_value(target_value)
                if (action == "add"):
                    self.get_regiter(target_register).set_value(
                        self.get_regiter(target_register).get_value() + target_value)
                if (action == "mul"):
                    self.get_regiter(target_register).set_value(
                        self.get_regiter(target_register).get_value() * target_value)
                if (action == "mod"):
                    self.get_regiter(target_register).set_value(self.get_regiter(target_register).get_value() % target_value)
                if (action == "snd"):
                    pair_program.recieve(self.get_regiter(target_register).get_value())
                    self.sent_count += 1
                if (action == "jgz"):
                    try:
                        reg_val = int(target_register)
                    except:
                        reg_val = self.get_regiter(target_register).get_value()
                    if (reg_val> 0):
                        increment_count = False
                        self.executing_instruction += target_value
                if (action == "rcv"):
                    if(len(self.queue) > 0):
                        self.get_regiter(target_register).set_value(self.get_from_queue())
                    else:
                        increment_count = False
                        self.is_waiting = True
                if (increment_count):
                    self.executing_instruction += 1


    def recieve(self,no):
        self.is_waiting = False
        self.queue.append(no)

    def get_from_queue(self):
        return self.queue.pop(0)

    def get_can_exit(self):
        if(self.is_waiting):
            return True
        if(self.is_terminated):
            return True
        return False
    #def get_value_in_reg(self):

    def get_sent(self):
        return self.sent_count