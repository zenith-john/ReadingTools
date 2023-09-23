# The script is used for filter the existing list by the user defined filter.
# The first argument is the filtered file and the second (optional) argument is language, "en" for English by default.
# The output file is filtered_list.txt.
import sys
if len(sys.argv) > 2:
    lang = sys.argv[2]
else:
    lang = "en"

if len(sys.argv) > 1:
    word_file = sys.argv[1]
else:
    print("No word list provided.")
    exit

lang = "en"
filter_file = "Filters/word_filter_" + lang + ".txt"
filter_list = []
output = "filtered_list.txt"

with open(filter_file, 'r') as fin:
    for line in fin.readlines():
        word = line.split()[0]
        if not word in filter_list:
            filter_list.append(word)

with open(word_file, 'r') as fin:
    with open(output, 'w') as fout:
        for line in fin.readlines():
            if line.split(" ")[0] not in filter_list:
                fout.write(line)
