from tablet import tablet
instructions = []
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
for idx, ins in enumerate(content):
    ins_list = []
    split = ins.split(" ")
    ins_list.append(split[0])
    try:
        ins_list.append(int(split[1]))
    except:
        ins_list.append(split[1])
    if(len(split) == 3):
        try:
            ins_list.append(int(split[2]))
        except:
            ins_list.append(split[2])
    else:
        ins_list.append(None)
    instructions.append(ins_list)

#print(instructions)
my_tablet = tablet(instructions)
has_termintated = False
count = 0
while(not has_termintated):
    my_tablet.execute_next_instruction()
    has_termintated = my_tablet.has_terminated()
    count += 1
print(my_tablet.get_sent())