import TextFileReader
import re

reader = TextFileReader.TextFileReader('Inputs\\input_day9.txt')
fileInput = reader.read_file()

def checkSum(input):
    # now create checksum
    checkSum = 0
    for i in range(len(input)- 1):
        if input[i] != '.':
            checkSum += i * input[i]
    return checkSum

def part1(input):
    # rearrangement for part 1
    for i in range(len(input)- 1):
        if input[i] == '.':
            for x in reversed(range(len(input))):
                if input[x] != '.' and x > i:
                    # swap position 
                    input[i], input[x] = input[x], input[i]
                    break
    return input

def findCharInList(input, target_char):
    groups = []
    current_group = []

    for index, item in enumerate(input):
        if item == target_char:
            current_group.append(index)  # Add the position of the target char
        else:
            if current_group:
                groups.append(current_group)  # Save the completed group
                current_group = []  # Reset the group
    if current_group:
        groups.append(current_group)  # Append the last group if it exists

    return [(len(group), group) for group in groups]

fileID = 0
newOutput = []
for i in range(len(fileInput)):
    length = []
    if i % 2 == 0:
        # its a file
        for x in range(int(fileInput[i])):
            length.append(fileID)
        fileID += 1
    else:
        for x in range(int(fileInput[i])):
            length.append('.')
    
    newOutput += length

# Target character
target_char = '.'

dotList = findCharInList(newOutput, target_char)
for length, position in dotList:
    numList = []
    for i in reversed(range(len(newOutput))):
        if (newOutput[i] != '.') and i > position[0]:
            if len(numList) == 0:
                numList = findCharInList(newOutput, newOutput[i])
            if i not in numList[0][1]:
                numList = findCharInList(newOutput, newOutput[i])
            if len(numList[0][1]) <= len(position):
                # switch positions
                newOutput[i], newOutput[position[0]]  = newOutput[position[0]], newOutput[i]
                position.pop(0)
                numList[0][1].pop()
                if len(position) == 0:
                    break

print(newOutput)
print(checkSum(newOutput))