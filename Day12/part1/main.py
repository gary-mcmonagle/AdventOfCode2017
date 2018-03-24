from program import program
from village import village
with open('input.txt','r') as f:
    programs = f.readlines()
programs = [x.strip() for x in programs]

my_village = village()

for idx,ind_program in enumerate(programs):
    id = int(ind_program.split("<->")[0].strip())
    pipes = ind_program.split("<->")[1].split(",")
    arr = []
    for p_idx,pipe in enumerate(pipes):
        arr.append(int(pipe.strip()))
    my_village.add_program(program(id,arr))

my_village.filter_groups()


print(my_village.get_groups()[0].get_member_size())
