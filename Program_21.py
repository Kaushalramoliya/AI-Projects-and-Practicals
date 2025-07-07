'''  
@author: 22000409 Kaushal Ramoliya  
@description: 21. - Create a model to predict next word conditional probability-based prediction model for 
Gujarati language (Download Gujarati text from sources available on the internet)
'''

import nltk
from nltk.util import ngrams
from collections import Counter, defaultdict
import random

with open('Program_21.txt', 'r', encoding='utf-8') as file:
    text = file.read()

tokens = nltk.word_tokenize(text)

bigrams = list(ngrams(tokens, 2))

bigram_counts = Counter(bigrams)
word_counts = Counter(tokens)

conditional_probabilities = defaultdict(dict)
for (w1, w2), count in bigram_counts.items():
    conditional_probabilities[w1][w2] = count / word_counts[w1]

def predict_next_word(word, conditional_probabilities):
    if word in conditional_probabilities:
        next_words = conditional_probabilities[word]
        predicted_word = max(next_words, key=next_words.get)
        return predicted_word, next_words[predicted_word]  
    else:
        return None, None

input_word = input("Enter a Gujarati word: ")
predicted_word, probability = predict_next_word(input_word, conditional_probabilities)

if predicted_word:
    print(f"The predicted next word is: {predicted_word}")
    print(f"Conditional probability of '{predicted_word}' given '{input_word}': {probability}")
else:
    print("No prediction available for the given word.")