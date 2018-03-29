from spin_lock import spin_lock
i = 1
my_sl = spin_lock(3)
while(i <= 400):
    my_sl.insert_value(i)
    print(my_sl.get_lock())
    #print(my_sl.get_lock())
    i += 1
    if(i%1000 == 0):
        print(i)
        #print(my_sl.get_lock())
print(my_sl.get_lock()[1])