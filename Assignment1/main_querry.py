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
    #file_id = 1
    for file in os.listdir():
        if file.endswith('.txt'):
            file_path = f"{path}{file}"
            posting = Postings(file_path, f"{file}")
            posting.add_to_dic(posting.normalization(posting.read_file()), postings_dictionary)
            #file_id += 1

    return dict(sorted(postings_dictionary.items()))


def find_and(diction, q1, q2):


    try:
        q1_p = diction[q1.lower()]
        q2_p = diction[q2.lower()]

        intersecton = Intersection(q1_p, q2_p)

        print(f'{q1} AND {q2} are in this/these documnet(s): {intersecton.intersect_and()}')

    except KeyError:
        print(f'The query is not found')


def find_or(diction, q1, q2):

    try:
        q1_p = diction[q1.lower()]
        q2_p = diction[q2.lower()]

        intersecton = Intersection(q1_p, q2_p)

        print(f'{q1} OR {q2} are in this/these documnet(s): {intersecton.intersect_or()}')

    except KeyError:
        print(f'The query is not found')


def find_not(diction, q1, q2):
    try:
        q1_p = diction[q1.lower()]
        q2_p = diction[q2.lower()]

        intersecton = Intersection(q1_p, q2_p)

        print(f'{q1} NOT {q2} are in this/these documnet(s): {intersecton.intersect_not()}')

    except KeyError:
        print(f'The query is not found')


def print_list(list_of_words):
    for w in list_of_words:
        print(w)


def main_menu(diction):
    while True:
        m_in = input('Do you have a query?')

        if m_in.lower() == 'yes':
            q_gate = ['and', 'or', 'not']

            q1 = input('Please insert a word:')
            print_list(q_gate)
            q3 = input('please make a choice:')
            if q3.lower() == q_gate[0]:
                q2 = input('Please enter another word:')
                find_and(diction, q1, q2)
            elif q3.lower() == q_gate[1]:
                q2 = input('Please enter another word:')
                find_or(diction, q1, q2)
            elif q3.lower() == q_gate[2]:
                q2 = input('Please enter another word:')
                find_not(diction, q1, q2)
            else:
                print('wrong choice')
                main_menu(diction)
        elif m_in.lower() == 'no':
            print('Thanks, hope you FoundIt :) !')
            sys.exit()
        else:
            print("Sorry I don't understand, would you please repeat again!")
            print('--------------------------------------------------------')
            print('--------------------------------------------------------')
            main_menu(diction)


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("usage: python3 main_querry.py FOLDER_PATH")
        exit()

    start = time()
    path = sys.argv[1]

    m = make_dic_postings(path)

    print("Time: (%.2f)s\n" % (time() - start), file=stderr)

    print('welcome to FindIt\n')
    print('-------------------------------------------\n')

    main_menu(m)
