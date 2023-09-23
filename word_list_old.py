import nltk
import os
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# from nltk.stem.lancaster import LancasterStemmer

def convert_tag(tag):
    if tag.startswith('J'):
        return "a"
    elif tag.startswith('V'):
        return "v"
    elif tag.startswith('N'):
        return "n"
    elif tag.startswith("R"):
        return "r"
    else:
        return "n"

corpus_path = "./Litteratures"
output = "output.txt"
count = Counter()

corpus = nltk.corpus.PlaintextCorpusReader(corpus_path, ".*\.txt")
print(corpus.fileids())

wnl = nltk.WordNetLemmatizer()
# lancaster_stemmer = LancasterStemmer()

tokens = corpus.words(corpus.fileids())
tokens = [word.lower() for word in tokens if word.isalpha()]
tokens = [word for word in tokens if word not in stopwords.words('english')]
tags = nltk.tag.pos_tag(tokens)
tokens = [wnl.lemmatize(tag[0], convert_tag(tag[1])) for tag in tags]
fdist = nltk.FreqDist(tokens)

with open(output, "w") as fout:
    for word, freq in fdist.most_common():
        fout.write(word + " " + str(freq) + "\n")

# with open(output, 'w') as fout:
#     for filepath,dirname,filenames in os.walk(corpus_path):
#         filenames = [filename for filename in filenames if filename.endswith(".txt")]
#         for filename in filenames:
#             print(filename)
#             with open(os.path.join(filepath, filename), 'r') as fin:
#                 text = fin.read()
