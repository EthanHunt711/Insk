import os
import sys
import numpy as np

from time import time
from sys import stderr
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
from numpy import dot
from numpy.linalg import norm

""" This program is an implementation of an information retrieval algorithm taking advantage of cosine similarity
between vectors of query and n documents where n=>1
The program is designed for reading a set of k txt files from a source folder where k=>1"""

lemmatizer = WordNetLemmatizer()
porter = PorterStemmer()
stop_words = set(stopwords.words('english'))


def tokenization(d):  # preprocessing the words in a single document
    token_list = []
    for line in d:
        for token in line.split():
            if token.isalpha():
                if token not in stop_words:
                    token_list.append(porter.stem(lemmatizer.lemmatize(token.lower())))
    return token_list


def text_tok(document):  # opening a file in order to preprocess
    with open(document, 'r', encoding='utf-8', errors='ignore') as d:
        return tokenization(d)


def doc_lists_to_word_set(doc_lists):  # creating a dictionary (word set)
    word_set = []
    for doc in doc_lists:
        for word in doc:
            word_set.append(word)
    return set(word_set)


def indexing(word_set):  # indexing the word set in order to use later in vectorization and extracting
    index_dict = {}
    i = 0
    for t in word_set:
        index_dict[t] = i
        i += 1
    return index_dict


def count(document, word_set):  # making a dictionary for counts of each token in a document
    count = {}
    for word in word_set:
        count[word] = 0
        for token in document:
            if token == word:
                count[word] += 1
    return count


def term_freq(document, count_dict, word_set):  # counting the term frequency for each document
    tf = {}
    for word in word_set:
        tf[word] = 0
        if word in document:
            tf[word] = round(count_dict[word]/len(document), 4)
    return tf


def idf(corpus, word_set):  # creating the inverse document frequency for each word in each document
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


def tf_idf(corpus, tf_dicts, idf_dict, index_dicts, word_set):  # assigning tf-idf weights to each token (vectorization)
    tf_idf_vectors = []
    for i, documemt in enumerate(corpus):
        tf_idf_vectors.append(np.zeros((len(word_set), )))
        for token in word_set:
            tf = tf_dicts[i][token]
            idf = idf_dict[token]

            tf_idf_weight = tf*idf
            tf_idf_vectors[i][index_dicts[token]] = round(tf_idf_weight, 4)
    return tf_idf_vectors


def query_to_corpus(query):  # creating a corpus out of the query
    query_corpus = []
    query_corpus.append([porter.stem(lemmatizer.lemmatize(token.lower())) for token in word_tokenize(query)])
    return query_corpus


def query_to_vector(query_corpus, idf_dicts, index_dicts, word_set):  # vectorizing the query

    query_count = count(query_corpus[0], word_set)

    query_tf = {}
    query_tf[0] = term_freq(query_corpus[0], query_count, word_set)

    query_tfidf = tf_idf(query_corpus, query_tf, idf_dicts, index_dicts, word_set)

    return query_tfidf


def cosine_similarity(query_vec, corpus):  # calculating cosine similarity based on the query and each document
    result_dict = dot(corpus, query_vec)/(norm(corpus)*norm(query_vec))

    return result_dict


def sort_dict_by_value(d, reverse=False):  # a sorting definition for sorting by value
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


def extract_cosine(q, iddf, index_dic, word_set, g, corpus_document_name):  # making a list of k top documents
    q_p = query_to_corpus(q)
    q_v = query_to_vector(q_p, iddf, index_dic, word_set)

    cosine_dict = {}
    for i in range(len(g)):
        cosine_dict[i] = cosine_similarity(q_v[0], g[i])
    co_di_s = sort_dict_by_value(cosine_dict, True)

    retrieved_documents = np.zeros((11,), dtype=int)
    for i in range(11):
        retrieved_documents[i] = list(co_di_s)[i]

    number = 1
    for x in list(co_di_s)[:10]:
        print(number, corpus_document_name[x])
        number += 1


def in_main(iddf, index_dic, word_set, g, corpus_document_name):  # menu in main
    while True:
        m_in = input('Do you have a query?')

        if m_in.lower() == 'yes':
            q = input('Please enter your query:')
            extract_cosine(q, iddf, index_dic, word_set, g, corpus_document_name)
            print('--------------------------------------------------------')
            print('--------------------------------------------------------')
            in_main(iddf, index_dic, word_set, g, corpus_document_name)
        if m_in.lower() == 'no':
            print('Thanks, hope you FoundIt :) !')
            sys.exit()
        else:
            print("Sorry I don't understand, would you please repeat again!")
            print('--------------------------------------------------------')
            print('--------------------------------------------------------')
            in_main(iddf, index_dic, word_set, g, corpus_document_name)


def main(path):  # the main method for reading from resources and returning the top k documents
    start = time()
    os.chdir(path)  # reading from the directory where txt files are stored

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
    print('-------------------------------------------\n')
    print("Loading Time: (%.2f)s\n" % (time() - start), file=stderr)
    print('-------------------------------------------\n')
    print('-------------------------------------------\n')

    in_main(iddf, index_dic, word_set, g, corpus_document_name)


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("usage: python3 cosine_top_k.py FOLDER_PATH")
        exit()

    path = sys.argv[1]

    print('Welcome to FindIt\n')
    print('-------------------------------------------\n')

    main(path)
