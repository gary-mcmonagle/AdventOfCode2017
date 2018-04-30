from program import program
with open("input.txt") as f:
    content = f.readlines()
#content = [x.strip() for x in content]
content = [x.split("=>") for x in content]
for idx, pat in enumerate(content):
    content[idx][0] = content[idx][0].strip()
    content[idx][1] = content[idx][1].strip()
my_program = program(content, ".#./..#/###")
print(my_program.get_on_pixels())
i = 0
while i < 2:
    my_program.do_iteration()
    i+=1
print(my_program.get_on_pixels())

#my_program.get_sub_grid()
g = [[1,2,3,10],[4,5,6,11],[7,8,9,12],[13,14,15,16]]
# #print(my_program.get_sub_grid(g,1,2))
# my_program.do_iteration()
# my_program.do_iteration()
#
# my_program.do_iteration()
# my_program.do_iteration()my_program.do_iteration()
# my_program.do_iteration()
print(my_program.get_pixels())