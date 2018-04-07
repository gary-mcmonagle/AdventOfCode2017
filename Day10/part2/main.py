from circular_list import circular_list
input_string = "flqrgnkx-0"
#input_string = "1,2,3"
lengths = []
for idx, num in enumerate(input_string):
    lengths.append(ord(num))
lengths.append(17)
lengths.append(31)
lengths.append(73)
lengths.append(47)
lengths.append(23)

my_list = circular_list(256)
my_list.perform_looped_hask_knot(lengths,64)
dense_hash = my_list.create_dense_hash()
my_string = ""
for idx, den in enumerate(dense_hash):
    var = str(hex(int(den)).rstrip("L").lstrip("0x") or "0")
    if len(var) == 1:
        var = "0"+var
    my_string += var
print(my_string)