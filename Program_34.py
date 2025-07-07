'''  
@author: 22000409 Kaushal Ramoliya  
@description: 34. - Write a program to create a POS tagger for English/Hindi/Gujarati language using DL model.
'''
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

def pos_tagger(text, model_name):
    # Load the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name)

    # Create a pipeline for token classification
    nlp_pipeline = pipeline("token-classification", model=model, tokenizer=tokenizer, grouped_entities=True)

    # Perform POS tagging
    results = nlp_pipeline(text)

    # Display the results
    print("POS Tagging Results:")
    for result in results:
        print(f"Word: {result['word']}, POS Tag: {result['entity_group']}")

# Example usage
if __name__ == "__main__":
    # Input text
    text = "આપણે બધા કૃત્રિમ બુદ્ધિ વિષય શીખી રહ્યા છે."  # Gujarati example
    # text = "हम सभी कृत्रिम बुद्धिमत्ता विषय सीख रहे हैं।"  # Hindi example
    # text = "We are all learning about artificial intelligence."  # English example

    # Choose a model (use multilingual model for Hindi/Gujarati)
    model_name = "Davlan/xlm-roberta-base-ner-hrl"  # Pre-trained multilingual model for low-resource languages

    # Perform POS tagging
    pos_tagger(text, model_name)