import TextFileReader
import re
from itertools import combinations

reader = TextFileReader.TextFileReader('Inputs\\example_day7.txt')
fileInput = reader.read_file()

fileInput = fileInput.splitlines()

# Define operations
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# List of operations in sequence
operations = [add, multiply]

# Function to perform operations
def operate_on_list(target, numbers, operations):
    results = []
    for i in range(len(numbers) - 1):
        for op in operations:
            result = op(numbers[i], numbers[i + 1])
            results.append((result, numbers[i], numbers[i + 1]))
    return results

numSum = 0
num = []
for line in fileInput:
    found = False
    result = line.replace(': ', ' ').split()
    # Convert the elements to integers
    result = [int(num) for num in result]
    # Check if the target can be formed
    possible = operate_on_list(result[0], result[1:], operations)
    print(possible)
    for new_Line in possible:
        new_Line = [int(num) for num in new_Line]
        if result[0] in new_Line:
            print("found")
        else:
            new_possible = operate_on_list(result[0], new_Line, operations)
    
            print(new_possible)


