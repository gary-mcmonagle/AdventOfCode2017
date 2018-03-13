import csv
list = []
csv_reader = csv.reader(open('input.csv', newline=''), delimiter=' ', quotechar='|')
for row in csv_reader:
    list.append(int(row[0]))

#list = [0, 3,  0,  1,  -3]
i = 0
jumps = 0
while(i < len(list)):
    jumps += 1
    num_steps = list[i]
    list[i] += 1
    i += num_steps

print(jumps)
