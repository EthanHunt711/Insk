from vocabulary import *
from count_dict import *
from tf_idf2 import *


def main(file):

    v = Vocabulary(file)

    sentences = v.text_to_sent_tokenize()
    word_set = v.make_set(v.sent_tokenize_to_word_set(sentences))

    word_count = Count_dict(word_set, sentences).count_dict()

    tf_idf = TF_IDF(v.number_of_doc(sentences), v.make_index(v.make_set(word_set)), word_count)

    vectors = []
    for sent in sentences:
        print(sent)
        vec = tf_idf.tf_idf(sent, word_set)
        vectors.append(vec)
    # an example
    print(vectors[0])
