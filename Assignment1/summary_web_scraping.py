import sys
import os
import re
from sys import argv, stderr
import string
import urllib.request

from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize


class Summary:
    def __init__(self, url_list):
        self.url_list = url_list

    def open_url(self, url):

        site_string = url
        site = urllib.request.urlopen(site_string)
        soup = BeautifulSoup(site, "html.parser")

        p_tags = soup.find_all("p")

        f_name = self.file_name(url)+'.txt'
        for p_tag in p_tags:
            if len(p_tag) == 1:
                if len(p_tag.text) > 50:
                    with open(f_name, 'a') as f:
                        f.write(p_tag.text + '\n')
                        f.close()

    def file_name(self, url):
        pre = ''.join(word_tokenize(BeautifulSoup(urllib.request.urlopen(url), "html.parser").title.string))
        return pre.translate(str.maketrans('', '', string.punctuation))

    def read_urls(self):
        for url in self.url_list:
            self.open_url(url)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: python3 summary_web_scraping.py LIST_FILE")
        exit()

    list_file = sys.argv[1]

    with open(list_file, 'r') as f:
        for line in f:
            summaries = Summary(line)
