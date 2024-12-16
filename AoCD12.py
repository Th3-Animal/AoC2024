import TextFileReader
import re

reader = TextFileReader.TextFileReader('Inputs\\example_day12.txt')
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

firstFound = re.search('R', fileInput)
print(firstFound)

for match in firstFound:
    print(match.pos)