from circular_list import circular_list
lengths = [94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243]
#lengths =[3, 4, 1, 5]
skip_size = 0
my_list = circular_list(256)
start_index = 0
for idx, length in enumerate(lengths):
    my_list.reverse_subsection(start_index, length)
    start_index = length + skip_size + start_index
    skip_size += 1
    if(start_index >= len(my_list.get_list())):
        minus_mult = int((start_index / (len(my_list.get_list()))))
        start_index = start_index-(len(my_list.get_list())*minus_mult)
print(my_list.get_list()[0]*my_list.get_list()[1])
#print(my_list.get_list())

#my_list.reverse_subsection(0, 3)