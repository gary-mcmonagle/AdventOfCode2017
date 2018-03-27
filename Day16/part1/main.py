from dance_troup import  dance_troup
f = open('input.txt','r')
moves = f.read().split(",")
my_troup = dance_troup()

# for idx, move in enumerate(moves):
#     my_troup.dance(move)
# my_troup.create_move_set()
# my_troup.reset_troup()
# evaluate_index = [10,100,1000,10000,100000,1000000]
i = 999999966
counter_size = 1
ev_counter = 0
while(i < 1000000000):
    for idx, move in enumerate(moves):
        my_troup.dance(move)
    if(my_troup.get_troup() == ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]):
        print("Match found at {}".format(i))
    i += 1
    if(i % 1000 == 0):
        print(i)




print(my_troup.get_troup())

