from nltk.tokenize import wordpunct_tokenize as nltk_tokenize
from nltk.stem.porter import PorterStemmer
# Note: install with pip install scikit-learn[alldeps]
from sklearn.feature_extraction.text import TfidfVectorizer
import unicodedata
import sys
from nltk.metrics.distance import edit_distance as nltk_edit_distance
from bs4 import BeautifulSoup

tbl = dict.fromkeys(i for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith('P'))


def remove_punctuation(text):
    return text.translate(tbl)


def compare(text1, text2):
    return tfidf(text1, text2), 0 # edit_distance(url1, url2)


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
    return (tfs*tfs.T).A[0,1]

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as myfile:
        html1=myfile.read()

    with open(sys.argv[2], 'r') as myfile:
        html2=myfile.read()

    text1 = BeautifulSoup(html1, "html.parser").get_text()
    text2 = BeautifulSoup(html2, "html.parser").get_text()
    tfidf_score, edit_distance_score = compare(text1, text2)
    print (str(tfidf_score)+" "+ str(edit_distance_score))
# To setup:
# pip install beautifulsoup4 nltk numpy request scikit-learn scipy sklearn
