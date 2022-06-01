import os
import sys
import numpy as np
import operator

from time import time
from sys import stdin, stderr
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
from numpy import dot
from numpy.linalg import norm

lemmatizer = WordNetLemmatizer()
porter = PorterStemmer()
stop_words = set(stopwords.words('english'))


def tokenization(d):
    token_list = []
    for line in d:
        for token in line.split():
            if token.isalpha():
                if token not in stop_words:
                    token_list.append(porter.stem(lemmatizer.lemmatize(token.lower())))
    return token_list


def text_tok(document):
    with open(document, 'r', encoding='utf-8', errors='ignore') as d:
        return tokenization(d)


def doc_lists_to_word_set(doc_lists):
    word_set = []
    for doc in doc_lists:
        for word in doc:
            word_set.append(word)
    return set(word_set)


def indexing(word_set):
    index_dict = {}
    i = 0
    for t in word_set:
        index_dict[t] = i
        i += 1
    return index_dict


def count(document, word_set):
    count = {}
    for word in word_set:
        count[word] = 0
        for token in document:
            if token == word:
                count[word] += 1
    return count


def term_freq(document, count_dict, word_set):
    tf = {}
    for word in word_set:
        tf[word] = 0
        if word in document:
            tf[word] = round(count_dict[word]/len(document), 4)
    return tf


def idf(corpus, word_set):
    df = {}
    idf = {}
    for word in word_set:
        df[word] = 0
        for document in corpus:
            if word in document:
                df[word] += 1
    for word in df:
        idf[word] = round(np.log10(len(corpus)/df[word]), 4)
    return idf


def tf_idf(corpus, tf_dicts, idf_dict, index_dicts, word_set):
    tf_idf_vectors = []
    for i, documemt in enumerate(corpus):
        tf_idf_vectors.append(np.zeros((len(word_set), )))
        for token in word_set:
            # if token in documemt:
            tf = tf_dicts[i][token]
            # else:
            #     tf = 0
            idf = idf_dict[token]

            tf_idf_weight = tf*idf
            tf_idf_vectors[i][index_dicts[token]] = round(tf_idf_weight, 4)
    return tf_idf_vectors

def query_to_corpus(query):
    query_corpus = []
    query_corpus.append([porter.stem(lemmatizer.lemmatize(token.lower())) for token in word_tokenize(query)])
    return query_corpus

def query_to_vector(query_corpus, idf_dicts, index_dicts, word_set):

    query_count = count(query_corpus[0], word_set)

    query_tf = {}
    query_tf[0] = term_freq(query_corpus[0], query_count, word_set)

    query_tfidf = tf_idf(query_corpus, query_tf, idf_dicts, index_dicts, word_set)

    return query_tfidf


def cosine_similarity(query_vec, corpus):
    # result_dict = {}
    # for i, document_vec in enumerate(corpus):
    result_dict = dot(corpus, query_vec)/(norm(corpus)*norm(query_vec))

    return result_dict


def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


def main(path):
    os.chdir(path)

    print("Loading files from " + path + "...", file=stderr)

    corpus_document_name = {}
    corpus = []
    count_dicts = {}
    tf_dicts = {}
    for i, file in enumerate(os.listdir()):
        if file.endswith('.txt'):
            file_path = f"{path}{file}"
            corpus.append(text_tok(file_path))
            corpus_document_name[i] = file

    word_set = doc_lists_to_word_set(corpus)

    for i in range(len(corpus)):
        count_dicts[i] = count(corpus[i], word_set)

    for i in range(len(corpus)):
        tf_dicts[i] = term_freq(corpus[i], count_dicts[i], word_set)

    iddf = idf(corpus, word_set)
    index_dic = indexing(word_set)

    g = tf_idf(corpus, tf_dicts, iddf, index_dic, word_set)

    q = input('Please enter your query:')
    q_p = query_to_corpus(q)
    q_v = query_to_vector(q_p, iddf, index_dic, word_set)

    # r = cosine_similarity(g[0], g[1])
    # t = cosine_similarity(g[0], g[2])
    # print(np.shape(q_v[0]))
    # print(np.shape(g[0]))
    cosine_dict = {}
    for i in range(len(g)):
        cosine_dict[i] = cosine_similarity(q_v[0], g[i])
    co_di_s = sort_dict_by_value(cosine_dict, True)


    number = 1
    for x in list(co_di_s)[:10]:
        print(number, corpus_document_name[x])
        number += 1
    # print(corpus_document_name)
    # print(type(q_v))
    # print(type(g))

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("usage: python3 main_querry.py FOLDER_PATH")
        exit()

    start = time()
    path = sys.argv[1]

    print("Time: (%.2f)s\n" % (time() - start), file=stderr)

    print('welcome to FindIt\n')
    print('-------------------------------------------\n')

    main(path)
