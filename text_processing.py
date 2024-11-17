import nltk
import time
import matplotlib.pyplot as plt
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Download necessary NLTK data
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')


# Sample text
data_text = 'data/healthcare.txt'

#Function to read text from file
def read_text_from_file(filepath):
    with open(filepath, 'r') as file:
        #text1 = file.readlines() ## Read the entire file content as a List
        text = file.read()  # Read the entire file content as a string
    return text



# Tokenization
def tokenize_text(text):
    return word_tokenize(text)

# Function for stemming with stopword removal
def stem_text(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    tokens = tokenize_text(text)
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words and word.isalpha()]
    stemmed_words = [ps.stem(word) for word in filtered_tokens]
    return stemmed_words

# Function for lemmatization with stopword removal
def lemmatize_text(text):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words and word.isalpha()]
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    return lemmatized_words

# Compare the time taken by stemming vs lemmatization
def compare_stemming_lemmatization(text):
    start = time.time()
    stemmed_words = stem_text(text)
    stem_time = time.time() - start

    start = time.time()
    lemmatized_words = lemmatize_text(text)
    lemmatize_time = time.time() - start

    print(f"Stemming Time: {stem_time:.6f} seconds")
    print(f"Lemmatization Time: {lemmatize_time:.6f} seconds")

    print("\nStemmed Words:", stemmed_words)
    print("\n\nLemmatized Words:", lemmatized_words)

    # Visualize the results
    words = ['Stemming', 'Lemmatization']
    times = [stem_time, lemmatize_time]

    plt.bar(words, times, color=['blue', 'green'])
    plt.xlabel('Method')
    plt.ylabel('Time in Seconds')
    plt.title('Stemming vs Lemmatization: Comparison of Processing Time')
    plt.show()

# Run the comparison
healthcare_text = read_text_from_file(data_text)

compare_stemming_lemmatization(healthcare_text)