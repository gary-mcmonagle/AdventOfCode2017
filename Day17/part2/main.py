from spin_lock import spin_lock
i = 1
my_sl = spin_lock(344)
while(i <= 50000000):
    my_sl.validate_first_element(i)
    if(i%10000 == 0):
        print(i)
    i += 1
print(my_sl.get_first_index())