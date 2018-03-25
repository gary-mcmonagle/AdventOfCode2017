from generator import generator

generator_a = generator(65,16807,4)
print(generator_a.get_next_value())
print(generator_a.get_next_value())

# generator_a = generator(277,16807)
# generator_b = generator(349,48271)
# count = 0
# idx = 0
# while(idx<40000000):
#     if(generator_a.get_value_as_lowest_binary() == generator_b.get_value_as_lowest_binary()):
#         #print("Match found!")
#         count += 1
#         print(count)
#     if(idx%100000 == 0):
#         print("idx at {}".format(idx))
#     idx += 1
#
# print(count)



