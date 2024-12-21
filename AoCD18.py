
import re
from collections import deque

fileInput = open('Inputs//input-day18.txt').read()

# create Grid
def create_grid(height, width, default_value):
	"""Create a grid with the given height and width, initialized with a default value."""
	return [[default_value for _ in range(width)] for _ in range(height)]

def update_grid(grid, row, col, new_value):
	"""Update the value at a specific position (row, col) in the grid."""
	if 0 <= row < len(grid) and 0 <= col < len(grid[0]):  # Ensure position is valid
		grid[row][col] = new_value
	else:
		print("Invalid position: Outside grid bounds")
		

# BFS to find the shortest path
def shortest_path_bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    queue = deque([(start, [start])])  # (current_position, path_to_position)
    visited = set()
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()

        # Check if we reached the end
        if (x, y) == end:
            return path

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check if the move is valid
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None  # No path found

gridHeight = 71
gridWidth = 71

fileInput = fileInput.splitlines()

grid = create_grid(gridHeight, gridWidth, '.')

timeToGo = 1024
for i, row in enumerate(fileInput):
	if i < timeToGo:
		x = int(row.split(',')[0])
		y = int(row.split(',')[1])
		update_grid(grid, y, x, '#')

start = (0, 0)
end = (gridHeight - 1, gridWidth - 1)

path = shortest_path_bfs(grid, start, end)

reachable = True
while reachable:
	# add another brick to the grid
    timeToGo += 1
    x = int (fileInput[timeToGo].split(',')[0])
    y = int (fileInput[timeToGo].split(',')[1])
    update_grid(grid, y, x, '#')

    path = shortest_path_bfs(grid, start, end)
    if path == None:
        reachable = False
        print(fileInput[timeToGo])

# print(len(path) - 1)  # type: ignore # Subtract 1 to exclude the starting position