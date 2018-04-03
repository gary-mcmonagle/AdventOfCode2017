from grid import grid
my_grid = grid()
i = 2
is_large_enough = False
while(not is_large_enough):
    my_grid.add_value(10)
    if(my_grid.get_last_value() > 277678):
        is_large_enough = True
        print(my_grid.get_last_value())
    i+=1

