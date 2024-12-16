import TextFileReader
import re

class AoCD3:
    pass
    
    def countXmas(fileInput, word):
        pattern = word
        matches = re.findall(pattern, fileInput)
        return len(matches)


if __name__ == "__main__":
    reader = TextFileReader.TextFileReader('example_d4.txt')
    fileInput = reader.read_file()

    # Word to search
    word = "XMAS|SAMX"

    # Count occurrences of XMAS
    # result = AoCD3.countXmas(fileInput, word)
    result = 0

    # Rotate the String
    lines = fileInput.splitlines()
    # rotated = ["".join(row).rstrip() for row in zip(*lines[::-1])]
    # rotated = "\n".join(rotated)

    # result += AoCD3.countXmas(rotated, word)

    # now for the diagonals
    inputArray = [list(line) for line in fileInput.splitlines()]
    for x in range(len(lines[0]) - 1):
        for y in range(len(inputArray) - 1):
            if inputArray[x][y] == "X":
                # check for directions
                # downwards right
                if y < (len(lines[0]) - 3) and x < (len(inputArray) - 3):
                    if inputArray[x+1][y+1] == "M":
                        if inputArray[x+2][y+2] == "A":
                            if inputArray[x+3][y+3] == "S":
                                result += 1

                # downwards left
                if y >= 3 and x <= len(inputArray) - 3:
                    if inputArray[x+1][y-1] == "M":
                        if inputArray[x+2][y-2] == "A":
                            if inputArray[x+3][y-3] == "S":
                                result += 1

                # upwards right
                if y <= len(lines[0]) - 3 and x >= 2 and x > 0 and y > 0:
                    if inputArray[x-1][y+1] == "M":
                        if inputArray[x-2][y+2] == "A":
                            if inputArray[x-3][y+3] == "S" and x-3 >= 0 and y - 3 >= 0:
                                result += 1

                # upwards left
                if y >= 2 and x >= 2 and x > 0 and y > 0:
                    if inputArray[x-1][y-1] == "M":
                        if inputArray[x-2][y-2] == "A":
                            if inputArray[x-3][y-3] == "S" and x-3 >= 0 and y - 3 >= 0:
                                result += 1
                
                # just upwards
                if x >= 2 and x > 0 and y > 0:
                    if inputArray[x-1][y] == "M":
                        if inputArray[x-2][y] == "A":
                            if inputArray[x-3][y] == "S" and x-3 >= 0:
                                result += 1
                
                #just downwards
                if x <= len(inputArray) - 3:
                    if inputArray[x+1][y] == "M":
                        if inputArray[x+2][y] == "A":
                            if inputArray[x+3][y] == "S":
                                result += 1
                
                # just forward
                if y <= len(lines[0]) - 3:
                    if inputArray[x][y+1] == "M":
                        if inputArray[x][y+2] == "A":
                            if inputArray[x][y+3] == "S":
                                result += 1

                #just backwards
                if y >= 2:
                    if inputArray[x][y-1] == "M":
                        if inputArray[x][y-2] == "A":
                            if inputArray[x][y-3] == "S":
                                result += 1

    print(result)