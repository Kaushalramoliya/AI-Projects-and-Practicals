'''  
@author: 22000409 Kaushal Ramoliya  
@description: 30. -  Write an Object Oriented Program which creates vocabulary of words and also counts each word in a document. 
Eg. Content 
The birds are flying. The boy is walking. The Ganges are great river system. The Narmada 
river flows from rift valley. 
output : 
[(The,3), (birds,1), (are,1), (birds,1), (are,2), (flying,1), (boy,1), (river,2)]
'''  
import re
from collections import Counter

class Vocabulary:
    def __init__(self, file_path):
        self.file_path = file_path
        self.word_counts = Counter()

    def process_document(self):
        # Read the file content
        with open(self.file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Remove punctuation and convert to lowercase
        content = re.sub(r'[^\w\s]', '', content).lower()

        # Tokenize the text into words
        words = content.split()

        # Count the frequency of each word
        self.word_counts = Counter(words)

    def get_vocabulary(self):
        # Return the vocabulary as a list of tuples (word, count)
        return list(self.word_counts.items())

    def display_vocabulary(self):
        # Display the vocabulary
        print("Vocabulary with Word Counts:")
        for word, count in self.word_counts.items():
            print(f"({word}, {count})")


# Example usage
file_path = "Program_30_input.txt"  # Replace with the path to your input file
vocab = Vocabulary(file_path)
vocab.process_document()
vocab.display_vocabulary()