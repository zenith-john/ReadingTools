# Introduction

This repository consists of several useful script for me in reading books. There are basically two functions, one for extracting new words from some texts, and another for planning the reading process.

## Prerequisite
- Python3
- [spaCy](https://spacy.io/) for Extracting Word List Flow

# Planning Flow
This flow is used when I want to nonlinear read a book, e.g. dictionary or book I have already read. This flow only requires one script, [reading_plan.py](). The script requires two argument, the first argument is the total number of the pages to read. The second argument can either be a number or a number plus string "day". In the first case, the number will be considered the pages you expected to read in one day. In the second case the number will be considered the number of days you want to finish reading.
```bash
python3 reading_plan.py 101 10 # Reading 101 pages with 10 pages a day
python3 reading_plan.py 101 10day # Reading 101 pages within 10 days
```

The output file is reading_plan.txt.

# Extracting Word List Flow
This flow is used when I decided to read some books in foreign language. To use it you need to install [spaCy](https://spacy.io/). The first step is put all text files in the Litterature directory. Then run [word_list.py](). The script accepts two optional arguments. The first is the language of the files. Only "en" (Default) for English and "fr" for French are supported yet. But you can add easily add support to other languages supported by [spaCy](https://spacy.io/). The second is the name of the output file which is "word_list\_" + lang + ".txt" by default.

```bash
python3 word_list.py en word_list_en.txt
```

After you get the word list, you can use [percentage_analysis.py]() to analyze how many words can cover 90%, 95%, 98%, 99% usage of the texts. And memorize frequently used words before reading. The script need an argument of the word list file name.

```bash
python3 percentage_analysis.py word_list_en.txt
```

Finally, before import word list into anki or other program, you can use [filter.py]() to remove those words you already know. The filter list should be placed under [Filters]() folder. It has one obligatory argument and one optional argument. First is the word list file name and second is the languge. The filter file should be named "word_filter_" + lang + ".txt". The output file is "filtered_list.txt".

```
python3 filter.py word_list_en.txt en
```

Then you can use filtered list to enlarge your vocabulary.

# History

The [word_list_old.py]() is the deprecated script to generate word list using nltk.

