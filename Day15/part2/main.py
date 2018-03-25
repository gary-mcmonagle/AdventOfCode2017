from generator import generator

generator_a = generator(277,16807,4)
generator_b = generator(349,48271,8)
count = 0
idx = 0
while(idx<5000000):
    if(generator_a.get_value_as_lowest_binary() == generator_b.get_value_as_lowest_binary()):
        count += 1
        print(count)
    if(idx%100000 == 0):
        print("idx = {}".format(idx))
    idx += 1

print(count)



