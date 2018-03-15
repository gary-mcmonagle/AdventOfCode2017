class program:
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

