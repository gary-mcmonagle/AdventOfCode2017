import csv
csv_reader = csv.reader(open('input.csv', newline=''), delimiter=' ', quotechar='|')
rows = []
for row in csv_reader:
    inner_list = row[0].split(",")
    for index, item in enumerate(inner_list):
        inner_list[index] = int(item)
    rows.append(inner_list)

def get_sum(row):
    got = False
    for i, outer in enumerate(row):
        for j, inner in enumerate(row):
             if(i != j):
                if(outer%inner == 0):
                    return int(outer/inner)
    if(got == False):
        print("Error no math")
total = 0
for index,row in enumerate(rows):
    total += get_sum(row)
print(total)

