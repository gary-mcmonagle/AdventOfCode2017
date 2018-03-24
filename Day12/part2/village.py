from group import group
class village:
    def __init__(self):
        self.programs = []
        self.groups = []
        self.visited = []

    def add_program(self, program):
        self.programs.append(program)

    def get_programs(self):
        return self.programs

    def has_been_visited(self,program):
        for idx, visited_program in enumerate(self.visited):
            if(program.equals(visited_program)):
                return True
        return False

    def get_program_by_id(self,id):
        for idx,program in enumerate(self.programs):
            if(program.get_id() == id):
                return program


    def add_to_group(self, program, group):
        if (not self.has_been_visited(program)):
            group.add_member(program)
            self.visited.append(program)
            self.visited.append(program)
            for idx, pipe in enumerate(program.get_pipes()):
                piped_prog = self.get_program_by_id(pipe)
                self.add_to_group(self.get_program_by_id(pipe),group)

    def add_group(self, program):
        my_group = group()
        if(not self.has_been_visited(program)):
            self.add_to_group(program,my_group)
            self.groups.append(my_group)

    def filter_groups(self):
        for idx, program in enumerate(self.programs):
            self.add_group(program)
    def get_groups(self):
        return self.groups
    def get_no_groups(self):
        return len(self.groups)



