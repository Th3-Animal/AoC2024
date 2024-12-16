import TextFileReader

class AoCD2:
    def checkList(entry):
        # check increment or decrement
        if entry[0] > entry[1]:
            # its a decrement
            for num in range(len(entry)-1):
                if entry[num] < entry[num + 1]:
                    return False

                else: 
                    if entry[num] - entry[num + 1] > 3 or entry[num] - entry[num + 1] == 0:
                        return False
                # if both if dont work it should be safe
            else:
                return True
                    
        else: 
            for num in range(len(entry)-1):
                if entry[num] > entry[num + 1]:
                    return False

                else: 
                    if entry[num + 1] - entry[num] > 3 or entry[num] - entry[num + 1] == 0:
                        return False
                # if both if dont work it should be safe
            else:
                return True
  

if __name__ == "__main__":
    reader = TextFileReader.TextFileReader('Input_Day2.txt')
    fileInput = reader.read_file()

    # Split sections based on new lines
    sections = [section.strip() for section in fileInput.split("\n") if section.strip()]
    # Convert each section into a list of numbers
    lists = [list(map(int, section.split())) for section in sections]

    # Check if safe or unsafe
    # Safe: increment or decrement by 1 up to 3
    # Unsafe: everything else
    safe = []
    for entry in lists:
        entrySafe = entry
        for y in range(len(entry)):
            entry = entrySafe.copy()
            entry.pop(y)
            if AoCD2.checkList(entry):
                if len(safe) == 0:
                    safe.append(y)
                    break
                else:
                    safe.append(y)
                    break
    
    print(len(safe))