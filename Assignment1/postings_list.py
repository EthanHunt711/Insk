import os
import sys
from sys import stdin, stderr
from time import time
from collections import defaultdict
from collections import OrderedDict
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer


class Postings:
    def __init__(self, document, document_id):
        self.document = document
        self.document_id = document_id

    def read_file(self):
        sorted_tokenized_doc = []
        with open(self.document, 'r', encoding='utf-8') as doc:
            for line in doc:
                for word in word_tokenize(line.lower()):
                    if word not in sorted_tokenized_doc:
                        sorted_tokenized_doc.append(word)
        return sorted(sorted_tokenized_doc)

    def normalization(self, tokenized_sentences):
        self.tokenized_sentences = tokenized_sentences
        stop_words = set(stopwords.words('english'))
        # ps = PorterStemmer()
        lem = WordNetLemmatizer()
        after_filter = []
        for tokenized in self.tokenized_sentences:
            if tokenized not in stop_words:
                after_filter.append(lem.lemmatize(tokenized))
        return sorted(after_filter)

    def add_to_dic(self, normalized_tokenized_voc_sorted, postings_diction):
        self.normalized_tokenized_voc_sorted = normalized_tokenized_voc_sorted
        self.postings_diction = postings_diction

        for w in self.normalized_tokenized_voc_sorted:
            if w in self.postings_diction.keys():
                self.postings_diction[w].extend(self.document_id)
            self.postings_diction[w] = [self.document_id]
        return self.postings_diction