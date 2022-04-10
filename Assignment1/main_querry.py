import sys
import os

from time import time
from sys import stdin, stderr
from collections import defaultdict
from postings_list import Postings


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("usage: python3 posting_list.py FOLDER_PATH")
        exit()

    start = time()
    path = sys.argv[1]

    os.chdir(path)

    print("Loading files from " + path + " ...", file=stderr)

    postings_dictionary = defaultdict(list)
    file_id = 1
    for file in os.listdir():
        if file.endswith('.en'):
            file_path = f"{path}{file}"
            posting = Postings(file_path, file_id)
            for tokened_w in posting.normalization(posting.read_file()):
                postings_dictionary[tokened_w].append(posting.document_id)
            file_id += 1
    q = dict(sorted(postings_dictionary.items()))
    print(q)
    print("Time: (%.2f)s\n" % (time() - start), file=stderr)