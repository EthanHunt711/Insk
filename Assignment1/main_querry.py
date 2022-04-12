import sys
import os

from time import time
from sys import stdin, stderr
from collections import defaultdict
from postings_list import Postings
from intersection import Intersection

def make_dic_postings(path):
    os.chdir(path)

    print("Loading files from " + path + " ...", file=stderr)

    postings_dictionary = defaultdict(list)
    file_id = 1
    for file in os.listdir():
        if file.endswith('.en'):
            file_path = f"{path}{file}"
            posting = Postings(file_path, file_id)
            posting.add_to_dic(posting.normalization(posting.read_file()), postings_dictionary)
            file_id += 1

    return dict(sorted(postings_dictionary.items()))


def find_and(diction):

    q1 = input('Please insert a word:')
    q2 = input('Please enter another word:')

    q1_p = diction[q1.lower()]
    q2_p = diction[q2.lower()]

    intersecton = Intersection(q1_p, q2_p)

    print(f'{q1} AND {q2} are in these documnet(s): {intersecton.intesect_and()}')



if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("usage: python3 posting_list.py FOLDER_PATH")
        exit()

    start = time()
    path = sys.argv[1]

    m = make_dic_postings(path)


    print("Time: (%.2f)s\n" % (time() - start), file=stderr)

    find_and(m)