from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer


class Vocabulary:
    def __init__(self, path):
        self.path = open(path, 'r', encoding='utf-8')

    def text_to_sent_tokenize(self):
        sentences = []
        lemmatizer = WordNetLemmatizer()
        stop_words = set(stopwords.words('english'))
        for sent in self.path:
            x = [lemmatizer.lemmatize(i.lower()) for i in word_tokenize(sent) if i.isalpha() and i not in stop_words]
            sentences.append(x)
        return sentences

    def sent_tokenize_to_word_set(self, sentences):
        self.sentences = sentences
        word_set = []
        for t_sent in self.sentences:
            for word in t_sent:
                if word not in word_set:
                    word_set.append(word)
        return word_set

    def make_set(self, word_set):
        self.word_set = word_set

        word_setted = set(self.word_set)
        return word_setted

    def number_of_doc(self, sentences):
        self.sentences = sentences
        number_of_doc = len(self.sentences)
        return number_of_doc

    def make_index(self, word_sett):
        self.word_sett = word_sett
        index_dict = {}
        i = 0
        for word in self.word_sett:
            index_dict[word] = i
            i += 1
        return index_dict
