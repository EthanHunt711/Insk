from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer


class Vocabulary:
    def __init__(self, path):
        self.path = open(path, 'r')

    def text_tokenize(self):
        token_list = []
        # lemmatizer = WordNetLemmatizer()
        # stop_words = set(stopwords.words('english'))
        for line in self.path:
            for token in line.split():
                if token.isalpha():
                    token_list.append(token.lower())
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
