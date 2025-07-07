'''  
@author: 22000409 Kaushal Ramoliya  
@description: 33. - Write a script to build Bag-of-Word and TF-IDF model from English text.
'''

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

#Sample English text data
documents = [
    "Natural Language Processing is a fascinating field.",
    "It involves the interaction between computers and human language.",
    "NLP techniques are used in applications like chatbots and sentiment analysis.",
    "The goal is to enable computers to understand and generate human language."
]

#Build Bag-of-Words (BoW) model
print("Bag-of-Words Model:")
vectorizer_bow = CountVectorizer()
bow_matrix = vectorizer_bow.fit_transform(documents)
print("Feature Names:", vectorizer_bow.get_feature_names_out())
print("BoW Matrix:\n", bow_matrix.toarray())

#Build TF-IDF model
print("\nTF-IDF Model:")
vectorizer_tfidf = TfidfVectorizer()
tfidf_matrix = vectorizer_tfidf.fit_transform(documents)
print("Feature Names:", vectorizer_tfidf.get_feature_names_out())
print("TF-IDF Matrix:\n", tfidf_matrix.toarray())