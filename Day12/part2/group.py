from program import program
class group:
    def __init__(self):
        self.members = []

    def is_member(self, program):
        for idx, member in enumerate(self.members):
            if(program.equals(member)):
                print("{0} already found in group".format(member.get_id()))
                return True
        return False

    def add_member(self, program):
        if(not self.is_member(program)):
            self.members.append(program)

    def get_member_size(self):
        return len(self.members)