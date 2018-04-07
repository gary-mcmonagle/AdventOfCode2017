from knot import knot
def to_bin(string):
    return_string = ""
    for idx, char in enumerate(string):
        try:
            val = bin(int(char, 16))[2:]
            while(len(val) < 4):
                val = "0" + val
            return_string += val
        except:
            None
    return return_string

hash_input = "amgozmfv-"
i = 0
count = 0
while i < 128:
    output = to_bin(knot.knot_hash(hash_input+str(i)))
    print(len(output))
    for idx, char in enumerate(output):
        if(char == "1"):
            count += 1
    i+=1
print(count)