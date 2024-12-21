import re
from collections import deque

fileInput = open('Inputs//example-day20.txt').read()

maze = fileInput.splitlines()

# Find the start (S) and end (E) positions
start = None
end = None
for r, row in enumerate(maze):
    for c, char in enumerate(row):
        if char == 'S':
            start = (r, c)
        elif char == 'E':
            end = (r, c)

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

# Solve the maze
path = shortest_path_bfs(maze, start, end)

# Output the result
if path:
    print("Shortest path found:")
    for step in path:
        print(step)
else:
    print("No path found!")
