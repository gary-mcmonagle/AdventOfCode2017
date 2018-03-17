import csv,os,json
from program import program

class programs:
    def get_input(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'input.csv')
        print(filename)
        csv_reader = csv.reader(open(filename, newline=''), delimiter=' ', quotechar='|')
        programs_list = []
        for row in csv_reader:
            program_name = row[0]
            end_index = row[1].find(')')
            program_weight = int(row[1][1:end_index])
            dependant_programs = []
            if (len(row) > 2):
                depends = row[3].split(',')
                for index, item in enumerate(depends):
                    if (not item == ''):
                        dependant_programs.append(item)
            programs_list.append(program(program_name, program_weight, dependant_programs))
        self.programs_list = programs_list

    def __init__(self):
        self.get_input()
        self.root = self.get_program_by_name(self.get_root_tower())

    def __getattr__(self, root):
        return self.root

    def __getattr__(self, programs_list):
        return self.programs_list

    def get_dependant_total_disk_weight(self, prog):
        total = 0
        for idx, dep in enumerate(prog.dependant_programs):
            total += self.get_program_by_name(dep).disk_weight
        return total

    def get_root_chain(self, prog):
        while(len(prog.dependant_programs) > 0):
            prog = self.get_program_by_name(prog.dependant_programs[0])
        return prog


    def get_parent_program(self,program_name):
        for index, program in enumerate(self.programs_list):
            to_return = False
            for dep_index, dep in enumerate(program.dependant_programs):
                if(dep == program_name):
                    to_return = True
            if(to_return):
                return program
                #return program(program.program_name, program.disk_weight, program.dependant_programs)

        return None

    def is_balanced(self, my_program):
        #print("Evaluating balance for {}".format(my_program.program_name))
        #for idx, dep in enumerate(my_program.dependant_programs):
            #print(self.get_program_by_name(dep).disk_weight)

        if(len(my_program.dependant_programs) == 0):
            return True
        else:
            measure = self.get_program_by_name(my_program.dependant_programs[0]).disk_weight
            #print("measure = {}".format(measure))
            for idx,dep in enumerate(my_program.dependant_programs):
                if(idx > 0):
                    my_var = self.get_program_by_name(dep)
                    #print(my_var.program_name)
                    #print(self.get_program_by_name(dep))
                    #print("measuring against: {}".format(my_var.disk_weight))
                    #print("measuring against: ".format(self.get_program_by_name(dep).disk_weight))
                    if(not (self.get_program_by_name(dep).disk_weight == measure)):
                        return abs(measure-self.get_program_by_name(dep).disk_weight)
            return True



    def get_root_tower(self):
        name = self.programs_list[0].program_name
        while(not name == None):
            value = name
            try:
                name = self.get_parent_program(name).program_name
            except:
                name = None
        return value

    def get_program_by_name(self, name):
        for idx, prog in enumerate(self.programs_list):
            if(prog.program_name == name):
                return prog

    def get_imbalance(self):
        for idx, prg in enumerate(self.programs_list):
            self.get_dependency_weight(prg)

    def update_program_list(self, program):
        for idx, prog in enumerate(self.programs_list):
            if(prog.program_name == program.program_name):
                self.programs_list[idx] = program

    def out_file(self, name):
        jsdata = {}
        for idx,prog in enumerate(self.programs_list):
            jsdata[prog.program_name]=[prog.disk_weight, prog.dependant_programs]
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, name)
        #parsed = json.loads(jsdata)
        with open(filename, 'w') as outfile:
            json.dump(jsdata, outfile, indent=4)
        #json.dumps(jsdata,filename )



    def get_dependency_weight(self, program):
        if(not program.has_been_visted):
            program.visit()
            #print(program.program_name)
            total = program.disk_weight
            for idx, dep in enumerate(program.dependant_programs):
                self.get_dependency_weight(self.get_program_by_name(dep))
            #print("{0} has a dependant weight of {1}".format(program.program_name,self.get_dependant_total_disk_weight(program)))
            #print(self.get_dependant_total_disk_weight(program) + program.disk_weight)
            program.set_disk_weight(self.get_dependant_total_disk_weight(program) + program.disk_weight)

            self.update_program_list(program)
            if(not self.is_balanced(program) == True):
                print(program.program_name)
                for idx,dep in enumerate(program.dependant_programs):
                    print("{0} has a disk weight of {1}".format(dep, self.get_program_by_name(dep).disk_weight))

                print(self.is_balanced(program))







my_programs = programs()
my_programs.out_file('before.json')
my_programs.get_imbalance()
my_programs.out_file('after.json')