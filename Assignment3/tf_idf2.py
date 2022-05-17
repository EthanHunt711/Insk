import numpy as np
import math


class TF_IDF:
    def __init__(self, total_document, index_dict, word_count):
        self.total_document = total_document
        self.index_dict = index_dict
        self.word_count = word_count

    def term_freq(self, document, word):
        self.document = document
        self.word = word

        N = len(self.document)
        print(N)
        occurrence = len([token for token in self.document if token == self.word])
        return 1 + np.log10(occurrence/N)

    def idf(self, word):
        self.word = word
        try:
            word_occurrence = self.word_count[self.word] + 1
        except:
            word_occurrence = 1

        return math.log10(self.total_document/word_occurrence)

    def tf_idf(self, sentence, word_set):
        self.sentence = sentence
        self.word_set = word_set
        tf_idf_vec = np.zeros((len(self.word_set),))
        for word in self.sentence:
            tf = self.term_freq(self.sentence, word)
            idf = self.idf(word)

            value = tf*idf
            tf_idf_vec[self.index_dict[word]] = value

        return tf_idf_vec