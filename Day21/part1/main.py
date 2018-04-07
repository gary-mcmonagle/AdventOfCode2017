from program import program
from collections import deque
with open("input.txt") as f:
    content = f.readlines()
#content = [x.strip() for x in content]
content = [x.replace("/","")for x in content]
content = [x.split("=>") for x in content]
for idx, pat in enumerate(content):
    content[idx][0] = content[idx][0].strip()
    content[idx][1] = content[idx][1].strip()
my_prog = program(content,".#...####")
my_prog.do_iteration()
my_prog.do_iteration()
my_prog.do_iteration()
my_prog.do_iteration()
my_prog.do_iteration()

print(my_prog.get_pixels().count("#"))



#print(content)
#
# def roll_list(li):
