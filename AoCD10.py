import TextFileReader
import sys

reader = TextFileReader.TextFileReader('Inputs\\input_day10.txt')
fileInput = reader.read_file()

def gridCreator(fileInput):
    grid = fileInput.splitlines()
    newGrid = []
    for line in grid:
        newLine = []
        for x in range(int(len(line))):
            newLine.append(int(line[x]))
        newGrid.append(newLine)
    return newGrid

def navigate_grid_iterative(grid, start):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    visited = set()
    path = []
    found = 0

    # Stack for DFS
    stack = [start]

    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue

        visited.add((x, y))
        path.append((x, y))

        # Current value at the position
        current_value = grid[x][y]
        if current_value == 9:
            found += 1

        # Add neighbors to the stack
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < rows and
                0 <= ny < cols and
                grid[nx][ny] == current_value + 1 and
                (nx, ny) not in visited
            ):
                stack.append((nx, ny))
    return path, found

def find_distinct_paths(grid, start):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    all_paths = []  # To store all distinct paths

    # Stack to store paths, each entry is a tuple (current_position, current_path)
    stack = [(start, [start])]

    while stack:
        (x, y), path = stack.pop()

        # Get the current value at the position
        current_value = grid[x][y]

        # Explore all valid neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < rows and
                0 <= ny < cols and
                grid[nx][ny] == current_value + 1 and
                (nx, ny) not in path  # Avoid revisiting nodes in the same path
            ):
                # Add the new path to the stack
                stack.append(((nx, ny), path + [(nx, ny)]))

        # If no neighbors are valid, this is an endpoint
        if all(
            not (0 <= x + dx < rows and 0 <= y + dy < cols and grid[x + dx][y + dy] == current_value + 1)
            for dx, dy in directions
        ):
            all_paths.append(path)

    return all_paths


# Example grid
grid = gridCreator(fileInput)
# find all starting positions
startingPoints = []
for x in range(len(grid[0])):
    for y in range(len(grid[x])):
        if grid[x][y] == 0:
            startingPoints.append((x,y))

allFound = 0
lenPath = 0
allPathes = []
for start in startingPoints:
    # Navigate the grid
    allPathes.append(find_distinct_paths(grid, start))

for path in allPathes:
    for innerPath in path:
        if len(innerPath) == 10:
            lenPath += 1

print(lenPath)
# Output results
print("Path of navigation:", len(allPathes))
