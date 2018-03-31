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
my_tablet.execute_instrutions()
#
# my_tablet.execute_instruction("set","a",2)
# my_tablet.execute_instruction("set","b",7)
# my_tablet.execute_instruction("add","b","a")
# my_tablet.execute_instruction("mul","b","a")
#
# print(my_tablet.get_registers()[1].get_value())