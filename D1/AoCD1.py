import TextFileReader
import BubbleSort

class AoCD1:
    def extractList(self, inputFile):
        # Split sections based on blank lines
        sections = [section.strip() for section in inputFile.split("\t") if section.strip()]

        # Convert each section into a list of numbers
        lists = [list(map(int, section.split())) for section in sections]
        return lists
           
    
if __name__ == "__main__":
    reader = TextFileReader.TextFileReader('Input_Day1.txt')
    fileInput = reader.read_file()

    lists = AoCD1.extractList(AoCD1, fileInput)
    # Separate numbers based on index
    even_index_list = [num for i, num in enumerate(lists[0]) if i % 2 == 0]
    odd_index_list = [num for i, num in enumerate(lists[0]) if i % 2 != 0]

    # now sort both lists
    sorter = BubbleSort.BubbleSort(even_index_list)
    even_index_list = sorter.sort()

    sorter = BubbleSort.BubbleSort(odd_index_list)
    odd_index_list = sorter.sort()

    totalDistance = 0
    for x in range(len(even_index_list)):
        if (even_index_list[x] > odd_index_list[x]):
            distance = even_index_list[x] - odd_index_list[x]
        else:
            distance = odd_index_list[x] - even_index_list[x]

        totalDistance = totalDistance + distance

    print(totalDistance)

    simiScore = 0
    for entry in even_index_list:
        amount = 0
        for num in odd_index_list:
            if(entry == num):
                amount += 1
        simiScore = simiScore + (entry * amount)

    print(simiScore)
            