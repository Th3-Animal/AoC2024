import TextFileReader
import re
from sympy import symbols, Eq, solve

reader = TextFileReader.TextFileReader('Inputs\\input_day13.txt')
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

# need a list entry for each button prize combination
fileInput = fileInput.splitlines()

newInput = []

i = 0
buttonPrize = {i: {}}



buttonPattern = r"(X\+(\d+))|(Y\+(\d+))"
prizePattern = r"(X\=(\d+))|(Y\=(\d+))"

for line in fileInput:
    # check the matches for X and Y
    if 'Button A' in line:
        matches = re.finditer(buttonPattern, line)
        for match in matches:
            if "X" in match.group():
                buttonPrize[i] = {
                'Xa': 0,
                'Ya': 0,
                'Xb': 0,
                'Yb': 0,
                'Xp': 0,
                'Yp': 0
                }
                buttonPrize[i]['Xa'] = int(match.group(2))
            elif "Y" in match.group():
                buttonPrize[i]['Ya'] =  int(match.group(4))
    if 'Button B' in line:
        matches = re.finditer(buttonPattern, line)
        for match in matches:
            if "X" in match.group():
                buttonPrize[i]['Xb'] = int(match.group(2))
            elif "Y" in match.group():
                buttonPrize[i]['Yb'] = int(match.group(4))
    elif 'Prize' in line:
        matches = re.finditer(prizePattern, line)
        for match in matches:
            if "X" in match.group():
                buttonPrize[i]['Xp'] = int(match.group(2))
            elif "Y" in match.group():
                buttonPrize[i]['Yp'] =  int(match.group(4))
        i += 1
  
# calculate for each entry in newInput the needed tokens
# extract everything
token = 0
prizeChange = 10000000000000
for x in range(len(buttonPrize.keys())):
    # Define symbols
    x1, x2 = symbols('x1 x2')

    # Define equations
    eq1 = Eq(buttonPrize[x]['Xa'] * x1 + buttonPrize[x]['Xb'] * x2, buttonPrize[x]['Xp'] + prizeChange)
    eq2 = Eq(buttonPrize[x]['Ya'] * x1 + buttonPrize[x]['Yb'] * x2, buttonPrize[x]['Yp'] + prizeChange)

    # Solve the equations
    solution = solve((eq1, eq2), (x1, x2))
    if solution[x1].is_integer and solution[x2].is_integer:
        token += solution[x1]*3 + solution[x2]*1

print(token)
