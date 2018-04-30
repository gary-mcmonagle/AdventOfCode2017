from enhancement_rule_book import enhancement_rule_book
from grid import grid
with open("input.txt") as f:
    content = f.readlines()
#content = [x.strip() for x in content]
content = [x.split("=>") for x in content]
for idx, pat in enumerate(content):
    content[idx][0] = content[idx][0].strip()
    content[idx][1] = content[idx][1].strip()

my_grid = grid("###/#../.#.", enhancement_rule_book(content))
i = 0
while i < 5:
    print(i)
    #print(my_grid.get_on_pixels())
    my_grid.do_iteration()
    print(my_grid.get_on_pixels())
    my_grid.do_grid_split()
    i+=1
