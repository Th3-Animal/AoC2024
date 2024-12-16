import re

fileInput = open('Inputs//input_day14.txt').read()

# create Grid
def create_grid(height, width, default_value):
	"""Create a grid with the given height and width, initialized with a default value."""
	return [[default_value for _ in range(width)] for _ in range(height)]

def create_quadrant(grid):
	# check for odd
	if len(grid)%2 != 0:
		mid_row = (len(grid))  // 2
		del(grid[mid_row])
	if len(grid[0])%2 != 0:
		mid_col = (len(grid[0])) // 2
		for row in grid:
			del(row[mid_col])
	
	# if not odd 
	mid_row = (len(grid))  // 2
	mid_col = (len(grid[0])) // 2

	Q1 = [row[:mid_col] for row in grid[:mid_row]]  # Top-left
	Q2 = [row[mid_col:] for row in grid[:mid_row]]  # Top-right
	Q3 = [row[:mid_col] for row in grid[mid_row:]]  # Bottom-left
	Q4 = [row[mid_col:] for row in grid[mid_row:]]  # Bottom-right
	return Q1, Q2, Q3, Q4
	
def update_grid(grid, row, col, new_value):
	"""Update the value at a specific position (row, col) in the grid."""
	if 0 <= row < len(grid) and 0 <= col < len(grid[0]):  # Ensure position is valid
		grid[row][col] = new_value
	else:
		print("Invalid position: Outside grid bounds")

def update_grid_number(grid, row, col, increment):
	"""Update the grid at the given position if . add 1"""
	if grid[row][col] == '.':
		if increment:
			grid[row][col] == 1
	else:
		# its a number
		if increment:
			grid[row][col] = int(grid[row][col]) + 1
		elif increment == False:
			grid[row][col] = int(grid[row][col]) - 1
			if grid[row][col] == '0' or grid[row][col] == 0:
				grid[row][col] = '.'
	
def teleport_movement(grid, start_row, start_col, move_row, move_col):
	"""Move within the grid with teleportation based on custom rules."""
	height = len(grid)
	width = len(grid[0])

	# Calculate new row
	new_row = start_row + move_row
	if new_row >= height:  # Exceeded positive y
		new_row = new_row - height
	elif new_row < 0:  # Exceeded negative y
		new_row = height - abs(new_row)

	# Calculate new column
	new_col = start_col + move_col
	if new_col >= width:  # Exceeded positive x
		new_col = new_col-width
	elif new_col < 0:  # Exceeded negative x
		new_col = width - abs(new_col)
		
	# decrement old grid pos
	update_grid_number(grid, start_row, start_col, False)
	
	# increment new grid pos
	update_grid_number(grid, new_row, new_col, True)

	return new_row, new_col
	
def print_Quadrants(Q1, Q2, Q3, Q4):
	# Print quadrants
	print("Q1 (Top-left):")
	for row in Q1:
		print(row)

	print("\nQ2 (Top-right):")
	for row in Q2:
		print(row)

	print("\nQ3 (Bottom-left):")
	for row in Q3:
		print(row)

	print("\nQ4 (Bottom-right):")
	for row in Q4:
		print(row)

def grid_to_string(grid):
	"""Convert the grid to a single string with elements separated by commas."""
	rows_as_strings = [",".join(map(str, row)) for row in grid]  # Convert each row to a string
	return "\n".join(rows_as_strings)  # Join rows with newline characters for re

def grid_to_string_clean(grid):
	"""Convert the grid to a single string with elements."""
	rows_as_strings = ["".join(map(str, row)) for row in grid]  # Convert each row to a string
	return "\n".join(rows_as_strings)  # Join rows with newline characters for re

def get_robots(grid):
	pattern = r'\d+'
	new_grid = grid_to_string(grid)
	matches = re.findall(pattern, new_grid)
	robSum = 0
	for match in matches:
		robSum += int(match[0])
	return robSum

# Example usage
height = 103
width = 101
grid = create_grid(height, width, default_value='.')

# create dict to save where every robot is with its move vector
robotDict = {}
# now the robot movement
sP_pattern = r'(p\=(\d+)\,(\d+))|(v\=(-?\d+)\,(-?\d+))'
pointMatches = re.findall(sP_pattern, fileInput)
i = 0 
for match in pointMatches:
	if 'p' in match[0]:
		robotDict[i] = {
		'pX': 0,
		'pY': 0,
		'vX': 0,
		'vY': 0
		}
		robotDict[i]['pX'] = int(match[1])
		robotDict[i]['pY'] = int(match[2])
	elif 'v' in match[3]:
		robotDict[i]['vX'] = int(match[4])
		robotDict[i]['vY'] = int(match[5])
		i += 1

# create starting grid
for i in range(len(robotDict)):
	x = robotDict[i]['pX']
	y = robotDict[i]['pY']
	if grid[y][x] != '.':
		if grid[y][x] == '1':
			update_grid(grid, y, x, '2')
		elif grid[y][x] == '2':
			update_grid(grid, y, x, '3')
		elif grid[y][x] == '3':
			update_grid(grid, y, x, '4')
	else:
		update_grid(grid, y, x, '1')

calculations = 100
# now for every move
for i in range(calculations):
	# for robot in range(1):
	for robot in range(len(robotDict)):
		robotDict[robot]['pY'], robotDict[robot]['pX'] = teleport_movement(grid,
															robotDict[robot]['pY'],
															robotDict[robot]['pX'],
															robotDict[robot]['vY'],
															robotDict[robot]['vX'])

# create grid
for i in range(len(robotDict)):
	x = robotDict[i]['pX']
	y = robotDict[i]['pY']
	if grid[y][x] != '.':
		if grid[y][x] == '1':
			update_grid(grid, y, x, '2')
		elif grid[y][x] == '2':
			update_grid(grid, y, x, '3')
		elif grid[y][x] == '3':
			update_grid(grid, y, x, '4')
	else:
		update_grid(grid, y, x, '1')
		
Q1, Q2, Q3, Q4 = create_quadrant(grid)

print_Quadrants(Q1, Q2, Q3, Q4)
safetyMeasure = get_robots(Q1) * get_robots(Q2) * get_robots(Q3) * get_robots(Q4)

print('Safety Measure: {0}'.format(safetyMeasure))
