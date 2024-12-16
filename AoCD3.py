import TextFileReader
import re

class AoCD3:
    pass


if __name__ == "__main__":
    reader = TextFileReader.TextFileReader('Input_Day3.txt')
    fileInput = reader.read_file()

    pattern = r"mul\(\d+\,\d+\)"

    matches = re.findall(pattern, fileInput)

    multiplication = 0
    for entry in matches:
        numMatch = re.findall(r"\d+", entry)
        multiplication += int(numMatch[0]) * int(numMatch[1])
    
    ##########
    # Part 2 #
    ##########

    doPattern = r"mul\(\d+\,\d+\)|do\(\)|don\'t\(\)"
    does = []
    # # find all do
    # for doMatch in re.finditer(doPattern, fileInput):
    #     does.append(doMatch.end())
    
    # print(does)

    # # find all don't
    # dontPattern = r"don\'t\(\)"
    # donts = []
    # for dontMatch in re.finditer(dontPattern, fileInput):
    #     donts.append(dontMatch.end())
    # print(len(donts))

    # multi = True
    # counter = 0
    # matchMul = []

    # for match in re.finditer(pattern, fileInput):
    #     for x in range(len(fileInput) - 1):
    #         if x >= counter:
    #             # find all matches till first dont
    #             # after that find next do and so on
    #             # while multi true add new matches to list
    #             if multi:
    #                 matchEnd = match.end()
    #                 if len(donts) > 0:
    #                     if x == donts[0]:
    #                         # delete all dos till this point
    #                         does = [x for x in does if x >= donts[0]]
    #                         del donts[0]
    #                         multi = False
    #                         counter = x
    #                         continue
    #                     elif x == match.end():
    #                         matchMul.append(match.group())
    #                         counter = x
    #                         break
    #             else:
    #                 # check for next do in list
    #                 if len(donts) > 0:
    #                     if x == does[0]:
    #                         multi = True
    #                         counter = x
    #                         continue
    
    # print(matchMul)
    # multiplication = 0
    # for entry in matchMul:
    #     numMatch = re.findall(r"\d+", entry)
    #     multiplication += int(numMatch[0]) * int(numMatch[1])
    # print(multiplication)

    multiplication = 0
    flag = True
    for match in re.findall(doPattern, fileInput):
        if match == "do()":
            flag = True
        elif match == "don't()":
            flag = False
        else:
            if flag:
                numMatch = re.findall(r"\d+", match)
                multiplication += int(numMatch[0]) * int(numMatch[1])
    print(multiplication)


    # 8326656
    # 9251848