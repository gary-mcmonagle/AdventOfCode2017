import csv
csv_reader = csv.reader(open('input4.csv', newline=''), delimiter=' ', quotechar='|')
rows = []
count = 0
def is_unique(item, list, index):
    for i, compare_item in enumerate(list):
        if(not i == index):
            #print("Comparing {0} AND {1}".format(item, compare_item))
            if(item == compare_item):
                print("Match found!")
                return False
    return True
for row in csv_reader:
    valid = True
    for i, item in enumerate(row):
        if(not (is_unique(item, row, i))):
            valid = False
    if(valid):
        count+=1

print(count)