from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer


class Vocabulary:
    def __init__(self, path):
        self.path = open(path, 'r', encoding='utf-8', errors='ignore')

    def text_tokenize(self):
        token_list = []
        lemmatizer = WordNetLemmatizer()
        porter = PorterStemmer()
        stop_words = set(stopwords.words('english'))
        for line in self.path:
            for token in line.split():
                if token.isalpha():
                    if token not in stop_words:
                        token_list.append(porter.stem(lemmatizer.lemmatize(token.lower())))
        return token_list

    def token_list_to_word_set(self, token_list):
        self.token_list = token_list
        return set(self.token_list)

    def make_index(self, word_set):
        self.word_set = word_set
        index_dict = {}
        i = 0
        for word in self.word_set:
            index_dict[word] = i
            i += 1
        return index_dict
