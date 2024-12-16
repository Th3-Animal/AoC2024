import tkinter as tk
from time import sleep

def parse_grid(grid_string):
    grid = [list(line) for line in grid_string.splitlines()]
    robot_pos = None
    boxes = set()
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == '@':
                robot_pos = (r, c)
            elif cell == 'O':
                boxes.add((r, c))
    return grid, robot_pos, boxes

def can_move_chain(grid, boxes, target, dr, dc):
    """Check if all boxes in the chain can move in the given direction."""
    while target in boxes:
        next_pos = (target[0] + dr, target[1] + dc)
        if grid[next_pos[0]][next_pos[1]] in ('#', 'O'):
            return False
        target = next_pos
    return True

def move_robot(grid, robot_pos, boxes, moves):
    """Simulate the robot's movement and yield the grid after each valid move."""
    directions = {
        '^': (-1, 0),  # Up
        'v': (1, 0),   # Down
        '<': (0, -1),  # Left
        '>': (0, 1)    # Right
    }
    
    for move in moves:
        dr, dc = directions[move]
        r, c = robot_pos
        target = (r + dr, c + dc)
        
        if grid[target[0]][target[1]] == '#':
            # Wall: do nothing
            continue
        
        if target in boxes:
            # If a box is in the way, check if it can be pushed
            if can_move_chain(grid, boxes, target, dr, dc):
                # Move the chain of boxes
                current = target
                while current in boxes:
                    next_pos = (current[0] + dr, current[1] + dc)
                    boxes.remove(current)
                    boxes.add(next_pos)
                    grid[current[0]][current[1]] = '.'  # Clear current box position
                    grid[next_pos[0]][next_pos[1]] = 'O'  # Move box to new position

                # Move robot to the target
                grid[r][c] = '.'  # Clear robot's old position
                grid[target[0]][target[1]] = '@'  # Move robot here
                robot_pos = target
                yield grid  # Yield the updated grid
            else:
                # Box can't move: do nothing
                continue
        else:
            # Empty space: move robot
            grid[r][c] = '.'  # Clear robot's old position
            grid[target[0]][target[1]] = '@'  # Move robot here
            robot_pos = target
            yield grid  # Yield the updated grid

# Tkinter visualization
class GridVisualizer(tk.Tk):
    def __init__(self, grid, cell_size=40):
        super().__init__()
        self.cell_size = cell_size
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.canvas = tk.Canvas(self, width=self.cols * cell_size, height=self.rows * cell_size)
        self.canvas.pack()
        self.title("Robot and Boxes")
    
    def draw_grid(self):
        """Draw the current state of the grid."""
        self.canvas.delete("all")  # Clear the canvas
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                x1, y1 = c * self.cell_size, r * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                
                if cell == '#':
                    color = "black"
                elif cell == '.':
                    color = "white"
                elif cell == '@':
                    color = "blue"
                elif cell == 'O':
                    color = "orange"
                else:
                    color = "white"
                
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
                if cell in {'@', 'O'}:
                    self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=cell, fill="black", font=("Arial", 16))
        self.update()

    def update_grid(self, grid):
        """Update the grid and redraw."""
        self.grid = grid
        self.draw_grid()

fileInput = open('Inputs//example-day15.txt').read()

# need to break up input into movement part containing ><v^ and grid
parts = fileInput.strip().split('\n\n')

input_grid = parts[0]
movement = parts[1]
moves = movement.replace('\n', '')


# Parse the grid and robot/move data
grid, robot_pos, boxes = parse_grid(input_grid.strip())

# Initialize the Tkinter visualizer
visualizer = GridVisualizer(grid)
visualizer.draw_grid()

# Simulate the moves and visualize the grid
def run_simulation():
    for updated_grid in move_robot(grid, robot_pos, boxes, moves):
        visualizer.update_grid(updated_grid)
        sleep(0.2)  # Pause to visualize each step

# Run the simulation in the Tkinter event loop
visualizer.after(100, run_simulation)
visualizer.mainloop()
