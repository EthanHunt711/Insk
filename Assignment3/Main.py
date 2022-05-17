import sys
import os
import fnmatch

from time import time
from sys import stdin, stderr
from collections import defaultdict
from vocabulary import *
from count_dict import *
from tf_idf2 import *


def main_menu(path):
    os.chdir(path)

    print("Loading files from " + path + "...", file=stderr)

    tfidf_dictionary = defaultdict(dict)
    document_id = 1
    corpus_count = len(fnmatch.filter(os.listdir(path), '*.txt'))
    print(corpus_count)
    for file in os.listdir():
        if file.endswith('.txt'):
            file_path = f"{path}{file}"
            v = Vocabulary(file_path)

            sentences = v.text_to_sent_tokenize()

            word_set = v.make_set(v.sent_tokenize_to_word_set(sentences))
            # print(document_id, word_set)
            word_count = Count_dict(word_set, sentences).count_dict()
            # print(document_id, word_count)
            # print(document_id, v.make_index(v.make_set(word_set)))
            tf_idf = TF_IDF(corpus_count, v.make_index(v.make_set(word_set)), word_count)
            for word in word_set:
                print(document_id, tf_idf.term_freq(sentences, word))
            tfidf_dictionary[document_id] = word_count
    #         for sentence in sentences:
    #             print(tf_idf.tf_idf(sentence, word_set))
            document_id += 1
    # print(tfidf_dictionary)




if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("usage: python3 main_querry.py FOLDER_PATH")
        exit()

    start = time()
    path = sys.argv[1]

    print("Time: (%.2f)s\n" % (time() - start), file=stderr)

    print('welcome to FindIt\n')
    print('-------------------------------------------\n')

    main_menu(path)


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
