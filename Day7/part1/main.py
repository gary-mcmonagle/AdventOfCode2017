import csv
from program import program

def parse_input():
    csv_reader = csv.reader(open('input.csv', newline=''), delimiter=' ', quotechar='|')
    programs = []
    for row in csv_reader:
        program_name = row[0]
        end_index = row[1].find(')')
        program_weight = int(row[1][1:end_index])
        dependant_programs = []
        if(len(row)>2):
            depends = row[3].split(',')
            for index, item in enumerate(depends):
                if(not item == ''):
                    dependant_programs.append(item)
        programs.append(program(program_name, program_weight, dependant_programs))
    return programs

def get_parent_program(programs, program_name):
    for index, program in enumerate(programs):
        to_return = False
        for dep_index, dep in enumerate(program.dependant_programs):
            if(dep == program_name):
                to_return = True
        if(to_return):
            return program.program_name
    return None

prog_input = parse_input()
name = prog_input[0].program_name
while(not name == None):
    value = name
    name = get_parent_program(prog_input, name)
print(value)