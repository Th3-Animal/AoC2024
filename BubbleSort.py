class BubbleSort:
    """Class to perform Bubble Sort on a list."""
    
    def __init__(self, data):
        """
        Initialize the BubbleSort class with the data to sort.
        
        :param data: A list of elements to sort.
        """
        self.data = data

    def sort(self):
        """
        Sorts the list in ascending order using Bubble Sort algorithm.
        
        :return: The sorted list.
        """
        n = len(self.data)
        for i in range(n):
            # Track if a swap occurred to optimize the algorithm
            swapped = False
            for j in range(0, n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    # Swap if the elements are in the wrong order
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    swapped = True
            # If no swaps occurred, the list is already sorted
            if not swapped:
                break
        return self.data

# Example usage:
if __name__ == "__main__":
    # Example list to sort
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    bubble_sorter = BubbleSort(unsorted_list)
    sorted_list = bubble_sorter.sort()
    print("Sorted List:", sorted_list)
