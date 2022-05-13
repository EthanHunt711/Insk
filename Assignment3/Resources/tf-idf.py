import time
from collections import defaultdict
from time import time
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords


class TF_IDF:

    def __init__(self, file, tf_dict):
        self.file = file
        self.tf_dict = tf_dict

    def tf(self):
        with open(self.file, encoding='utf-8') as f:
            for line in f:
                for t in word_tokenize(line.lower()):
                    if t not in self.tf_dict:
                        self.tf_dict[t] = 1
                    self.tf_dict[t] += 1
        return self.tf_dict

    def idf(self):
        pass

    def to_vec(self, vec_dic):
        list_of_words = []
        self.vec_dic = vec_dic
        stop_words = set(stopwords.words('english'))
        with open(self.file, encoding='utf-8') as f:
            for line in f:
                for t in word_tokenize(line.lower()):
                    if t not in stop_words:
                        list_of_words.append(t)

            for line in f:
                for t in word_tokenize(line.lower()):
                    if t not in list_of_words:
                        vec_dic[line].append(0)
                    vec_dic[line].append(1)
            return vec_dic