from generator import generator


generator_a = generator(277,16807)
generator_b = generator(349,48271)
count = 0
idx = 0
while(idx<40000000):
    if(generator_a.get_value_as_lowest_binary() == generator_b.get_value_as_lowest_binary()):
        count += 1
        print(count)
    if(idx%100000 == 0):
    idx += 1

print(count)



