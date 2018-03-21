from hex_grid import hex_grid
#my_grid = hex_grid()
f = open('input.txt','r')
moves = f.read().split(",")
my_grid = hex_grid(moves)
diag = my_grid.get_diagonal(my_grid.get_direction(my_grid.get_co_ord()), my_grid.get_co_ord())
print(abs(my_grid.get_co_ord()[0] - diag[0][0])+ diag[1])
