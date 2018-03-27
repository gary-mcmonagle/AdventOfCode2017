from spin_lock import spin_lock
i = 1
my_sl = spin_lock(344)
while(i <= 2017):
    print(my_sl.insert_value(i))
    i += 1
print(my_sl.get_lock())