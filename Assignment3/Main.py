import sys
import os
import fnmatch

from time import time
from sys import stdin, stderr
from collections import defaultdict

import numpy as np

from vocabulary import *
from count_dict import *
from tf_idf2 import *


def list_of_list_to_set(lists):
    word_set = []
    for l in lists:
        for w in l:
            word_set.append(w)
    return set(word_set)


def main_ve(path):
    os.chdir(path)

    print("Loading files from " + path + "...", file=stderr)

    # tfidf_dictionary = defaultdict(dict)
    document_id = 1
    corpus_count = len(fnmatch.filter(os.listdir(path), '*.txt'))
    corpus_document_names = {}
    corpus_token_lists = []
    word_set_sets = {}
    u_word_set = []
    corpus_index_dicts = {}
    corpus_count_dicts = {}
    term_freq_dicts = {}
    for file in os.listdir():
        if file.endswith('.txt'):
            file_path = f"{path}{file}"

            corpus_document_names[document_id] = f"{file}"

            vocabulary = Vocabulary(file_path)
            token_list = vocabulary.text_tokenize()
            corpus_token_lists.append(token_list)

            word_set = vocabulary.token_list_to_word_set(token_list)
            index_dict = vocabulary.make_index(word_set)
            count_dict = Count_dict(word_set, token_list).count_dict()

            word_set_sets[document_id] = word_set

            u_word_set.append(token_list)
            corpus_index_dicts[document_id] = index_dict
            corpus_count_dicts[document_id] = count_dict

            tf_idf = TF_IDF(corpus_count, count_dict)

            term_freq_dicts[document_id] = tf_idf.term_freq(token_list, count_dict)

            document_id += 1
    u_word_set = list_of_list_to_set(u_word_set)

    tf_idf_c = TF_IDF(corpus_count, corpus_count_dicts)

    i = tf_idf_c.word_count_per_document(u_word_set, corpus_token_lists)
    idf_dict = tf_idf_c.idf(i, corpus_count)

    vectors_dict = {}
    for i, t_lst in enumerate(corpus_token_lists):
        v = tf_idf_c.tf_idf(corpus_token_lists[i], word_set_sets[i+1], term_freq_dicts[i+1], idf_dict,
                            corpus_index_dicts[i+1])
        vectors_dict[i+1] = v

    print(vectors_dict[1][0], corpus_token_lists[0][0])


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("usage: python3 main_querry.py FOLDER_PATH")
        exit()

    start = time()
    path = sys.argv[1]

    print("Time: (%.2f)s\n" % (time() - start), file=stderr)

    print('welcome to FindIt\n')
    print('-------------------------------------------\n')

    main_ve(path)


# def main(file):
#
#     v = Vocabulary(file)
#
#     sentences = v.text_to_sent_tokenize()
#     word_set = v.make_set(v.sent_tokenize_to_word_set(sentences))
#
#     word_count = Count_dict(word_set, sentences).count_dict()
#
#     tf_idf = TF_IDF(v.number_of_doc(sentences), v.make_index(v.make_set(word_set)), word_count)
#
#     vectors = []
#     for sent in sentences:
#         vec = tf_idf.tf_idf(sent, word_set)
#         vectors.append(vec)
#     # an example
#     print(vectors)
