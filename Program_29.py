'''  
@author: 22000409 Kaushal Ramoliya  
@description: 29. -  Write an Object-Oriented Program which reads texts from a file. It must display file 
statistics a below. 
a. No. of sentences. 
b. No. of words. 
c. No. of total characters (Does not include whitespace) 
d. No. of whitespaces 
e. Total no. of digits, uppercase and lowercase letters.
'''  
class TextFileAnalyzer:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.text = ""
        self.stats = {
            "sentences": 0,
            "words": 0,
            "characters": 0,
            "whitespaces": 0,
            "digits": 0,
            "uppercase_letters": 0,
            "lowercase_letters": 0
        }

    def read_file(self):
        try:
            with open(self.input_file, 'r', encoding='utf-8') as file:
                self.text = file.read()
        except FileNotFoundError:
            print(f"Error: File '{self.input_file}' not found.")

    def analyze(self):
        self.stats["sentences"] = self.text.count('.') + self.text.count('!') + self.text.count('?')
        self.stats["words"] = len(self.text.split())
        self.stats["whitespaces"] = self.text.count(' ')
        self.stats["characters"] = len([c for c in self.text if not c.isspace()])
        self.stats["digits"] = sum(c.isdigit() for c in self.text)
        self.stats["uppercase_letters"] = sum(c.isupper() for c in self.text)
        self.stats["lowercase_letters"] = sum(c.islower() for c in self.text)

    def write_output(self):
        with open(self.output_file, 'w', encoding='utf-8') as file:
            file.write(f"Number of sentences: {self.stats['sentences']}\n")
            file.write(f"Number of words: {self.stats['words']}\n")
            file.write(f"Number of total characters (excluding whitespace): {self.stats['characters']}\n")
            file.write(f"Number of whitespaces: {self.stats['whitespaces']}\n")
            file.write(f"Total number of digits: {self.stats['digits']}\n")
            file.write(f"Total number of uppercase letters: {self.stats['uppercase_letters']}\n")
            file.write(f"Total number of lowercase letters: {self.stats['lowercase_letters']}\n")

    def process(self):
        self.read_file()
        self.analyze()
        self.write_output()

if __name__ == "__main__":
    analyzer = TextFileAnalyzer("Program_29_input.txt", "Program_29_output.txt")
    analyzer.process()


