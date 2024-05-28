import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('rslp')
# nltk.download('mac_morpho')
# from nltk.stem.porter import PorterStemmer
from nltk.stem import RSLPStemmer
import numpy as np

# stemmer = PorterStemmer()
stemmer = RSLPStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence, language='portuguese')

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype = np.float32)
    for index, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[index] = 1.0

    return bag

