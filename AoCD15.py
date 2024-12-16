import re

fileInput = open('Inputs//example-day15.txt').read()

# need to break up input into movement part containing ><v^ and grid
parts = fileInput.strip().split('\n\n')

grid = parts[0]
movement = parts[1]

def splitInHalf(number):
    # Convert to string
    num_str = str(number)
    slicer = int(len(num_str)/2)
    first_half = int(num_str[:slicer])
    second_half = int(num_str[slicer:])
    return first_half, second_half

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

def parse_bigger_grid(grid_string):
    grid = [list(line) for line in grid_string.splitlines()]
    robot_pos = None
    boxes = set()
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == '@':
                robot_pos = (r, c)
            elif cell == '[]':
                boxes.add((r, c))
    return grid, robot_pos, boxes

def display_grid(grid):
    for row in grid:
        print("".join(row))

def expand_map(original_map):
    # Define transformation rules for each tile
    transformation = {
        '#': '##',
        'O': '[]',
        '.': '..',
        '@': '@.'
    }
    
    # Process each row in the map
    expanded_map = []
    for row in original_map:
        expanded_row = "".join(transformation[tile] for tile in row)
        expanded_map.append(expanded_row)
    
    return expanded_map

def move_robot(grid, robot_pos, boxes, moves):
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
        
        elif target in boxes:
            # If a box is in the way, determine the chain of boxes
            chain = [target]
            while True:
                next_box = (chain[-1][0] + dr, chain[-1][1] + dc)
                if next_box in boxes:
                    chain.append(next_box)
                else:
                    break
            
            # Check if the last position in the chain is valid
            final_target = (chain[-1][0] + dr, chain[-1][1] + dc)
            if grid[final_target[0]][final_target[1]] not in ('#', 'O'):
                # Move all boxes in the chain
                for box in reversed(chain):
                    next_pos = (box[0] + dr, box[1] + dc)
                    boxes.remove(box)
                    boxes.add(next_pos)
                    grid[box[0]][box[1]] = '.'  # Clear current box position
                    grid[next_pos[0]][next_pos[1]] = 'O'  # New box position
                
                # Move the robot
                grid[r][c] = '.'  # Clear robot's old position
                grid[target[0]][target[1]] = '@'  # Move robot here
                robot_pos = target
            else:
                # Chain cannot move: do nothing
                continue
        else:
            # Empty space: move robot
            grid[r][c] = '.'  # Clear robot's old position
            grid[target[0]][target[1]] = '@'  # Move robot here
            robot_pos = target
    
    return grid

def move_robot_big(grid, robot_pos, boxes, moves):
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
        
        elif target in boxes:
            # If a box is in the way, determine the chain of boxes
            chain = [target]
            while True:
                next_box = (chain[-1][0] + dr, chain[-1][1] + dc)
                if next_box in boxes:
                    chain.append(next_box)
                else:
                    break
            
            # Check if the last position in the chain is valid
            final_target = (chain[-1][0] + dr, chain[-1][1] + dc)
            if grid[final_target[0]][final_target[1]] not in ('#', '[]'):
                # Move all boxes in the chain
                for box in reversed(chain):
                    next_pos = (box[0] + dr, box[1] + dc)
                    boxes.remove(box)
                    boxes.add(next_pos)
                    grid[box[0]][box[1]] = '.'  # Clear current box position
                    grid[next_pos[0]][next_pos[1]] = '[]'  # New box position
                
                # Move the robot
                grid[r][c] = '.'  # Clear robot's old position
                grid[target[0]][target[1]] = '@'  # Move robot here
                robot_pos = target
            else:
                # Chain cannot move: do nothing
                continue
        else:
            # Empty space: move robot
            grid[r][c] = '.'  # Clear robot's old position
            grid[target[0]][target[1]] = '@'  # Move robot here
            robot_pos = target
    
    return grid

def grid_to_string_clean(grid):
	"""Convert the grid to a single string with elements."""
	rows_as_strings = ["".join(map(str, row)) for row in grid]  # Convert each row to a string
	return "\n".join(rows_as_strings)  # Join rows with newline characters for re

def find_crates(gridStr):
    grid, robot_pos, boxes = parse_grid(gridStr)
    # crates or boxes are O
    coordinates = 0
    for pos in boxes:
        coordinates += 100 * pos[0] + pos[1]
    
    return coordinates

movement = movement.replace('\n', '')

grid, robot_pos, boxes = parse_grid(grid)
grid = expand_map(grid)
grid, robot_pos, boxes = parse_bigger_grid(grid_to_string_clean(grid))

new_grid = move_robot(grid, robot_pos, boxes, movement)

display_grid(new_grid)