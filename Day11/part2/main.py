from hex_grid import hex_grid
#my_grid = hex_grid()
f = open('input.txt','r')
moves = f.read().split(",")
my_grid = hex_grid(moves)
print(my_grid.get_largest_distance())
