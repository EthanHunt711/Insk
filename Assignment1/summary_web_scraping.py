import os
import re
import nltk
import string
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from collections import defaultdict
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
