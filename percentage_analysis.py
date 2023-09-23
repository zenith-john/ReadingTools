# Analyze the word coverage.
# The arguemnt is required for the word list file name.
import sys

if len(sys.argv) > 1:
    input_file = sys.argv[1]

    perc = [0.9, 0.95, 0.98, 0.99, 1.01]

    with open(input_file, "r") as fin:
        texts = fin.readlines()
        num = len(texts)
        words = [""] * num
        count = [0] * num
        for i in range(0, num):
            l = texts[i].split()
            words[i] = l[0]
            count[i] = int(l[1])
        for i in range(1, num):
            count[i] += count[i - 1]
        ptr = 0
        complete = count[num - 1]
        for i in range(0, num):
            while count[i] >= complete * perc[ptr]:
                print(words[i] + " " + str(perc[ptr] * 100) + "%")
                ptr += 1
