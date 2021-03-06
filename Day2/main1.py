import csv
csv_reader = csv.reader(open('input.csv', newline=''), delimiter=' ', quotechar='|')
rows = []
for row in csv_reader:
    inner_list = row[0].split(",")
    for index, item in enumerate(inner_list):
        inner_list[index] = int(item)
    rows.append(inner_list)

def get_difference(row):
    lowest = row[0]
    highest = row[0]
    for index, item in enumerate(row):
        if(item > highest):
            highest = item
        if(item < lowest):
            lowest = item
    return highest-lowest
total = 0
for index,row in enumerate(rows):
    total += get_difference(row)
print(total)

