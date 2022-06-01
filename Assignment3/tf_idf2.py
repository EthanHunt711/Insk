import numpy as np


class TF_IDF:
    def __init__(self, total_document, word_count):
        self.total_document = total_document
        self.word_count = word_count

    def term_freq(self, document, count_dict):
        self.count_dict = count_dict
        self.document = document
        term_freq_dict = {}

        N = len(self.document)
        for word in self.document:
            term_freq_dict[word] = self.count_dict[word] / N

        return term_freq_dict

    def word_count_per_document(self, u_word_set, corpus_lists):
        w_c_p_d_dict = {}
        self.u_word_set = u_word_set
        self.corpus_lists = corpus_lists
        for word in self.u_word_set:
            w_c_p_d_dict[word] = 0
            for document in self.corpus_lists:
                if word in document:
                    w_c_p_d_dict[word] += 1

        return w_c_p_d_dict

    def idf(self, w_c_p_d_dict, n_documents):
        self.w_c_p_d_dict = w_c_p_d_dict
        self.n_documents = n_documents
        idf_dict = {}

        for word in self.w_c_p_d_dict:
            idf_dict[word] = self.n_documents/self.w_c_p_d_dict[word]

        return idf_dict

    def tf_idf(self, document, word_set, term_freq_dict, idf_dict, idx_dict):
        self.document = document
        self.word_set = word_set
        self.term_freq_dict = term_freq_dict
        self.idf_dict = idf_dict
        self.idx_dict = idx_dict
        tf_idf_vec = np.zeros((len(self.word_set),))
        for word in self.document:
            tf = 1 + np.log(self.term_freq_dict[word])
            idf = np.log10(self.idf_dict[word])

            weight = tf * idf
            tf_idf_vec[self.idx_dict[word]] = round(weight, 2)

        return tf_idf_vec
