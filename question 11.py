import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

# Sentence to tokenize and remove stop words from
sentence = "Natural language processing is a subfield of artificial intelligence."

# Tokenize the sentence
words = word_tokenize(sentence)

# Get a set of English stop words
stop_words = set(stopwords.words('english'))

# Remove stop words
filtered_words = [word for word in words if word.lower() not in stop_words]

# Join the filtered words to create a new sentence
filtered_sentence = ' '.join(filtered_words)

# Print the result
print("Original Sentence:", sentence)
print("Filtered Sentence:", filtered_sentence)
