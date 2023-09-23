import collections
import os
import spacy
import sys

if len(sys.argv) > 1:
    lang = sys.argv[1]
else:
    lang = "en"

if lang == "en":
    nlp = spacy.load("en_core_web_sm")
elif lang == "fr":
    nlp = spacy.load("fr_core_news_sm")
# elif lang == "jp":
#    nlp = spacy.load("ja_core_news_sm")
else:
    print("Language not supported.")
    exit

if len(sys.argv) > 2:
    output = sys.argv[2]
else:
    # default output_file
    output = "word_list_" + lang + ".txt"

corpus_path = "./Litteratures"

cnt = collections.Counter()

for filepath,dirname,filenames in os.walk(corpus_path):
    filenames = [filename for filename in filenames if filename.endswith(".txt")]
    for filename in filenames:
        print(filename)
        with open(os.path.join(filepath, filename), 'r') as fin:
            text = fin.read()
            for txt in text.split('\n\n'):
                doc = nlp(txt)
                lemmas = [token.lemma_.lower() for token in doc if token.text.isalpha()]
                cnt = cnt + collections.Counter(lemmas)

with open(output, 'w') as fout:
    for tup in cnt.most_common():
        fout.write(tup[0] + " " + str(tup[1]) + "\n")
