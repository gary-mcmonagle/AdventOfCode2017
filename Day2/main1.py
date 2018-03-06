import csv
spamReader = csv.reader(open('input.csv', newline=''), delimiter=' ', quotechar='|')
rows = []
for row in spamReader:
    innerList = row[0].split(",")
    for index, item in enumerate(innerList):
        innerList[index] = int(item)
    rows.append(innerList)

def getDifference(row):
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
    total += getDifference(row)
print(total)

