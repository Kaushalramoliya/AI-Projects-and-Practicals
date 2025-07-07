'''  
@author: 22000409 Kaushal Ramoliya  
@description: 31. - Develop an NLP application which tokenizes text, removes punctuation marks, converts to 
lower case, removes spelling errors, removes stopwords, convert to root word using either 
stemmer or lemmatizer and displays counts/frequency of the main text words.
'''
import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
import nltk


# Step 1: Read input text
with open('Program_31_input.txt', 'r') as file:
    text = file.read()

# Step 2: Convert to lowercase
text = text.lower()

# Step 3: Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Step 4: Correct spelling using TextBlob
corrected_text = str(TextBlob(text).correct())

# Write corrected text to output.txt
with open('Program_31_output.txt', 'w') as file:
    file.write(corrected_text)

# Step 5: Tokenize corrected text
tokens = word_tokenize(corrected_text)

# Step 6: Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]

# Step 7: Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

# Step 8: Count word frequencies
word_counts = Counter(lemmatized_tokens)

# Step 9: Display word frequencies
print("Processed Words with Frequencies:\n")
for word, freq in word_counts.items():
    print(f"{word}: {freq}")
