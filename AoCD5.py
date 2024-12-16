import TextFileReader
from functools import cmp_to_key

def find_middle(input):
    length = len(input)
    if length % 2 == 0: 
        middle = length/2
        return int(middle-1) # minus 1 because of the start at 0
    else:
        length += 1
        middle = length/2
        return int(middle-1) # minus 1 because of the start at 0

def checkOrder(input, rule):
    r = rule.split('|')
    if r[0] in input and r[1] in input:
        # check for indizes
        uI1 = input.index(r[0])
        uI2 = input.index(r[1])
        if r[0] > r[1]:
            if uI1 < uI2:
                # rule true
                pass
            else:
                return False
        else:
            if uI1 < uI2:
                # rule true
                pass
            else:
                return False
    return True

reader = TextFileReader.TextFileReader('Inputs\\example_day5.txt')
fileInput = reader.read_file()

# Rules are all Combinations before the Blank line
lines = fileInput.splitlines()

rules = []
updates = []
for line in lines:
    if "|" in line:
        rules.append(line)
    elif "," in line:
        updates.append(line)

midSum = 0
falseOrdered = []
'''
Check each update with each Rule
if both numbers are in the Update check whether the rule is true or false
'''
for update in updates:
    rightOrder = True
    for rule in rules:
        r = rule.split('|')
        if r[0] in update and r[1] in update:
            # check for indizes
            uI1 = update.index(r[0])
            uI2 = update.index(r[1])
            if r[0] > r[1]:
                if uI1 < uI2:
                    # rule true
                    pass
                else:
                    falseOrdered.append(update)
                    rightOrder = False
                    break
            else:
                if uI1 < uI2:
                    # rule true
                    pass
                else:
                    falseOrdered.append(update)
                    rightOrder = False
                    break
    # if we got to this point we can summarize the mid number
    if rightOrder:
        midSum += int(update.split(',')[find_middle(update.split(','))])

midSum = 0
# we need to sort the false Ordered Elements
for update in falseOrdered:
    rightOrder = True
    # split list to order it
    newList = update.split(',')
    # permutations work to long
    # now we can start over with our checks          
    for rule in rules:
        r = rule.split('|')
        if r[0] in newList and r[1] in newList:
            for y in range(len(newList) - 1):
                newList = update.split(',')
                # check for indizes
                uI1 = newList.index(r[0])
                uI2 = newList.index(r[1])
                if r[0] > r[1]:
                    if uI1 < uI2:
                        rightOrder = True
                        break                      
                    else:
                        # switch order
                        newList[y], newList[y+1] = newList[y + 1], newList[y]
                        rightOrder = False
                        continue
                else:
                    if uI1 < uI2:
                        rightOrder = True
                        break                     
                    else:
                        # switch order
                        newList[y], newList[y+1] = newList[y + 1], newList[y]
                        rightOrder = False
                        continue 
            
            # if no rule
    # if we got to this point we can summarize the mid number
    if rightOrder:
        midSum += int(newList[find_middle(newList)])
        continue
        
print(midSum)

rules, pages = open('Inputs\\Input_Day5.txt').read().split('\n\n')
cmp = cmp_to_key(lambda x, y: -(x+'|'+y in rules))

a = [0, 0]
for p in pages.split():
    p = p.split(',')
    s = sorted(p, key=cmp)
    a[p!=s] += int(s[len(s)//2])

print(*a)
                    