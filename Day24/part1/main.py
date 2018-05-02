from bridge_maker import bridge_maker
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
c_list = []
for idx, c in enumerate(content):
    c_list.append([int(c.split("/")[0]), int(c.split("/")[1])])

my_maker = bridge_maker(c_list)
my_maker.generate_bridges(my_maker.get_component_list(), 0, 0)
print(my_maker. get_largest_bridge())