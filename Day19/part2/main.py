from route import route
with open("input.txt") as f:
    content = f.readlines()
maze = []
for idx, line in enumerate(content):
        maze.append(list(line))
longest = 0
for idx,line in enumerate(maze):
    if(len(line) > len(maze[longest])):
        longest = idx
for idx,line in enumerate(maze):
    if(line[len(line)-1] == '\n'):
        line.pop()
for idx,line,in enumerate(maze):
    if(len(line) < len(maze[longest])):
        i = 0
        diff = len(maze[longest]) - len(line)
        while(i < diff):
            maze[idx].append(" ")
            i+=1

my_route = route(maze)
print(my_route.send_packet())