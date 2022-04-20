import re
import nltk
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from collections import defaultdict
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize

my_page = '''
<!DOCTYPE html>
<html>
<head>
    <title>My Title</title>
</head>
<body>

    <h1>My First Heading</h1>
    <p>My first paragraph.</p>

    <h1>My Second Heading</h1>
    <p>My second paragraph.</p>

</body>
</html> 
'''

# Search for the title of the page

heading_search = re.compile(r'<h1.*>(.+)</h1>')
heading = heading_search.findall(my_page)
paragraph_search = re.compile(r'<p.*>(.+)</p>')
paragraph = paragraph_search.findall(my_page)

soup = BeautifulSoup(my_page, "html.parser")

# print(heading)
# print(paragraph)
# print(soup)
# print(soup.prettify())
# print(soup.title)
# print(soup.h1)
# print(soup.title.get_text())
# print(soup.h1.get_text())

site_string = "https://www.sparknotes.com/lit/animaldreams/summary/"

jn_site = urllib.request.urlopen(site_string)
soup2 = BeautifulSoup(jn_site, "html.parser")

# print(soup2.title.string)

site_string2 = "https://www.sparknotes.com/lit/animaldreams/summary/"

site3 = urllib.request.urlopen(site_string2)
soup3 = BeautifulSoup(site3, "html.parser")

# print(soup3.title.string)

site_string3 = "https://www.sparknotes.com/lit/animaldreams/summary/"
site4 = urllib.request.urlopen(site_string3)
soup4 = BeautifulSoup(site4, "html.parser")
# print(soup4.prettify())
# print(soup4.title.string)

a_tags = soup4.find_all("a")
# print(a_tags)

# for t in a_tags:
  # print(t)

p_tags = soup4.find_all("p")
# print(p_tags)
# print(type(p_tags))

#for p_tag in p_tags:
   # print(p_tag.text)

chomsky_text = ""
for p_tag in p_tags:
    chomsky_text += p_tag.text
# print(chomsky_text)

chomsky_tokens = sent_tokenize(chomsky_text)
for line in chomsky_tokens:
    print(line)
print(chomsky_tokens)

pos_tagged_chomsky = nltk.pos_tag(chomsky_tokens)

# print(pos_tagged_chomsky)

vowels = "aeiouy"

def count_vowels(word,vs):
    n = 0
    for char in word:
        if char in vs:
            n += 1
    return n

vowels_wordLength = {}

for w in chomsky_tokens:
    vowels_wordLength[count_vowels(w, vowels)] = len(w)

for k, v in vowels_wordLength.items():
    # print(k, v)
    pass

df = pd.DataFrame(list(vowels_wordLength.items()), columns=['Vowels', 'Characters'])

# print(df)

# scatter1 = sns.regplot(x="Vowels", y="Characters", data=df)
# plt.show()
