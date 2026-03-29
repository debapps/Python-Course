from os import strerror, path

class FileHandler:
    def __init__(self, file_path):
        self.file_path = path.normpath(file_path)  # Normalize the file path
        self.base_name = path.basename(self.file_path)  # Extract the file name
        self.file_name = path.splitext(self.base_name)[0] # Extract the file name without extension
        self.output_file_name = f"{self.file_name}.hist"  # Output file name
        self.output_file_path = path.join('data/output', self.output_file_name)  # Output file path

    def read_file(self):
        try:
            with open(self.file_path, 'rt', encoding='utf-8') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except Exception as e:
            print(f"Error reading file: {strerror(e.errno)}")

    def write_output(self, data):
        try:
            with open(self.output_file_path, 'wt', encoding='utf-8') as file:
                for letter, count in data.items():
                    file.write(f"{letter} -> {count}\n")
            print(f"File Letter Histogram written to '{self.output_file_path}'")
        except Exception as e:
            print(f"Error writing to file: {strerror(e.errno)}")

class LetterCountter:
    def __init__(self, text):
        self.text = text

    def count_letters(self):
        letter_count = {}
        for char in self.text:
            if char.isalpha():  # Check if the character is a letter
                char = char.lower()  # Convert to lowercase for uniformity
                if char in letter_count:
                    letter_count[char] += 1
                else:
                    letter_count[char] = 1
        return letter_count
    

if __name__ == "__main__":

    file_path = input("Enter the path of the file to read: ")
    file_handler = FileHandler(file_path)
    content = file_handler.read_file()
    
    if content:
        letter_counter = LetterCountter(content)
        counts = letter_counter.count_letters()
        
        # sort the counts by counts
        counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

        file_handler.write_output(counts)

