class TextFileReader:
    def __init__(self, file_path):
        """
        Initialize the TextFileReader with the path to the text file.
        
        :param file_path: Path to the text file to read.
        """
        self.file_path = file_path

    def read_file(self):
        """
        Reads the content of the text file and returns it as a string.
        
        :return: Content of the file as a string.
        :raises FileNotFoundError: If the file does not exist.
        :raises IOError: If there is an error reading the file.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{self.file_path}' does not exist.")
        except IOError as e:
            raise IOError(f"An error occurred while reading the file: {e}")

# Example usage:
if __name__ == "__main__":
    # Replace 'example.txt' with the path to your text file
    reader = TextFileReader('Input_Day1.txt')
    try:
        content = reader.read_file()
        print("File Content:")
        print(content)
    except Exception as e:
        print(e)
