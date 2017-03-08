import requests
import argparse
import os
#import nltk
import ssl
import html2text
from nltk.tokenize import wordpunct_tokenize as nltk_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.downloader import download
# Note: install with pip install scikit-learn[alldeps]
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.spatial.distance import cosine
import unicodedata
import sys
from nltk.metrics.distance import edit_distance as nltk_edit_distance

tbl = dict.fromkeys(i for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith('P'))

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


def remove_punctuation(text):
    return text.translate(tbl)


def compare(url1, url2):
    return tfidf(url1, url2)


def edit_distance(text1, text2):
    return nltk_edit_distance(remove_punctuation(text1.lower()), remove_punctuation(text2.lower()))


def tokenize(text):
    clean_text = remove_punctuation(text.lower())
    tokens = nltk_tokenize(clean_text)
    stemmed_tokens = []
    stemmer = PorterStemmer()
    for item in tokens:
        stemmed_tokens.append(stemmer.stem(item))
    return stemmed_tokens


def tfidf(text1, text2):
    tf_idf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    tfs = tf_idf.fit_transform([text1, text2])
    return cosine(tfs[0].todense(), tfs[1].todense())


# def url_to_filename(url):
#     filename = url
#     if filename.startswith('http://'):
#         filename = filename[7:]
#     if filename.startswith('https://'):
#         filename = filename[8:]
#     if filename.endswith('/'):
#         filename = filename[:-1]
#     filename = filename.replace('.', '_')
#     filename = filename.replace('/', '-')
#     return filename


#def setup_nltk():
#    download('stopwords')

if __name__ == '__main__':

    with open(sys.argv[1], 'r') as myfile:
        data1=myfile.read()

    with open(sys.argv[2], 'r') as myfile:
        data2=myfile.read()

    tfidf_score = compare(data1, data2)
    print (str(tfidf_score))

