from computing_cluster import computing_cluster
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = [list(x) for x in content]

my_cluster = computing_cluster(content)
i = 0
while i < 10000:
    print(i)
    my_cluster.do_burst()
    i+=1
print(my_cluster.get_infected_count())
# print()
# my_cluster.grow_grid()
# for idx, row in enumerate(my_cluster.get_cluster()):
#     print(row)