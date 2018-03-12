import csv
csv_reader = csv.reader(open('input4.csv', newline=''), delimiter=' ', quotechar='|')
rows = []
count = 0

def is_anagram(word_1, word_2):
    list_word_1 = list(word_1)
    list_word_2 = list(word_2)
    if(len(word_1) == len(word_2)):
        i = 0
        while(i < len(list_word_1)):
            found = False
            j = 0
            while(j < len(list_word_2)):
                if(not found):
                    if(list_word_1[i] == list_word_2[j]):
                        list_word_1.pop(i)
                        list_word_2.pop(j)
                        i -= 1
                        found = True
                j+=1
            i+=1
        if(len(list_word_1) == 0):
            print("Anagram found")
            return True
        else:
            return False
    else:
        return False


def is_unique(item, list, index):
    for i, compare_item in enumerate(list):
        if(not i == index):
            #print("Comparing {0} AND {1}".format(item, compare_item))
            if(is_anagram(item, compare_item)):
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

#print(is_anagram("hello", "gary"))