from grid import grid
my_grid = grid()
i = 2
while(i <= 277678):
    print(i)
    my_grid.add_value(i)
    #print(my_grid.get_nodes())
    i+=1

print(my_grid.get_nodes())
print(my_grid.get_origin())
print(my_grid.get_distance())
