class program:
    has_been_visted = False

    def __init__(self, program_name, disk_weight, dependant_programs):
        self.program_name = program_name
        self.disk_weight = disk_weight
        self.dependant_programs = dependant_programs

    def __getattr__(self, program_name):
        return self.program_name

    def __getattr__(self, disk_weight):
        return self.disk_weight
    def __getattr__(self, dependant_programs):
        return self.dependant_programs

    def set_disk_weight(self, weight):
        self.disk_weight = weight

    def __getattr__(self, has_been_visted):
        return has_been_visted
    def visit(self):
        self.has_been_visted = True

    def copy(self):
        return program(self.program_name, self.disk_weight, self.dependant_programs)

