import TextFileReader
import re

reader = TextFileReader.TextFileReader('Inputs\\input_day6.txt')
fileInput = reader.read_file()

''' 
Need to find ^ it shows the facing direction 
possible directions:
^ - up
> - right
< - left 
v - down

# - obstacle, need to turn right

. - free space
'''

directions = ['up', 'right', 'down', 'left']

def find_direction(matrix):
    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            # find the ^ 
            if matrix[y][x] == '^':
                return y, x, "up", '^'
            elif matrix[y][x] == '<':
                return y, x, "left", "<"
            elif matrix[y][x] == '>':
                return y, x, "right", ">"
            elif matrix[y][x] == 'v':
                return y, x, "down", "v"
    return None

# funtion to move the "guard"
def move_guard(matrix):
    if find_direction(matrix) == None:
        return None
    y, x, direction, moveSymbol = find_direction(matrix)
    # calc new pos
    if direction == "up":
        new_x, new_y = x, y - 1
    elif direction == "left":
        new_x, new_y = x - 1, y
    elif direction == "right":
        new_x, new_y = x + 1, y
    elif direction == "down":
        new_x, new_y = x, y + 1
    else:
        print("Invalid direction")
        return None
    
    len_x = len(matrix[x])
    len_y = len(matrix)
    
    # Check Bounds
    if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and (matrix[new_y][new_x] == "." or matrix[new_y][new_x] == "X"):
        # Mark old position
        matrix[y][x] = "X" 
        # Move to new position
        matrix[new_y][new_x] = moveSymbol
    # check for obstacle
    elif 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and matrix[new_y][new_x] == "#":
        # dont move change direction rightwards
        if direction == 'up':
            matrix[y][x] = ">"
        elif  direction == 'right':
            matrix[y][x] = "v"
        elif direction == 'down':
            matrix[y][x] = '<'
        elif direction == 'left':
            matrix[y][x] = '^'
    # check for leavin the map  
    elif new_x <= 0 or new_y <= 0 or new_x > len_x -1 or new_y > len_y - 1:
        # Mark old position
        matrix[y][x] = "X" 
        print("Guard has left")
        return matrix, False
    else:
        print("Invalid Move")
        return None

    return matrix, True
# Split the string into a 2D array
matrix = [list(row) for row in fileInput.splitlines()]

move = True
while (move):
    matrix, move = move_guard(matrix)

    # for line in enumerate(matrix):
    #   print(line)

# now count the X
countX = 0
for y, row in enumerate(matrix):
    counter = re.findall('X', ''.join(row))
    for match in counter:
        countX += 1

print(countX)