import spacy
import nltk

# Example sentence
sentence = "The quick brown fox jumps over the lazy dog."

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Perform POS tagging
tagged = nltk.pos_tag(tokens)

# Print all adjectives
adjectives = [word for word, pos in tagged if pos in ['JJ', 'JJR', 'JJS']]
print(adjectives)

