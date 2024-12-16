import TextFileReader

reader = TextFileReader.TextFileReader('Inputs\\example_day11.txt')
fileInput = reader.read_file()

def integerLength(number):
    return (len(str(number)))

def gridCreator(fileInput):
    grid = fileInput.splitlines()
    newGrid = []
    for line in grid:
        newLine = []
        for x in range(int(len(line))):
            newLine.append(int(line[x]))
        newGrid.append(newLine)
    return newGrid

def getListInt(fileInput):
    result = fileInput.split(' ')
    result = [int(num) for num in result]
    return result

def splitInHalf(number):
    # Convert to string
    num_str = str(number)
    slicer = int(len(num_str)/2)
    first_half = int(num_str[:slicer])
    second_half = int(num_str[slicer:])
    return first_half, second_half

def findOccur(inputDict, number):
    try:
        if number in inputDict[number]:
            inputDict['occur'] = inputDict['occur'] + 1
        else:
            inputDict['occur'] = 1
    except:
        inputDict['occur'] = 1

fileInput = getListInt(fileInput)
inputDict = {}

for num in fileInput:
    inputDict[num] = 1
    
print(len(inputDict))
# number of blinks 
for i in range(6):
    jumpOne = False
    x = 0
    while (x < len(inputDict)):
        # check for application of rules
        if jumpOne:
            # need this for the second rule
            jumpOne = False
            x += 1
            continue
        elif fileInput[x] == 0:
            fileInput[x] = 1
        elif integerLength(fileInput[x])%2 == 0:
            first, second = splitInHalf(fileInput[x])
            fileInput[x] = first
            fileInput.insert(x+1, second)
            jumpOne = True
        else:
            fileInput[x] = fileInput[x] * 2024
        x += 1

print(len(fileInput))