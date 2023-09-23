# Read a book in random order. Example: Dictionary
# By default, the first argument is the number of total pages and the another argument is what you expected to read one day.
# However if the second argument ends with 'day' or 'days', then it means you decide to read up the book in that number of days.
# The output file is reading_plan.txt
import random
import sys
from math import ceil

if len(sys.argv) < 2:
    print("No enough arguments.")
    exit

output = "reading_plan.txt"
total_page = int(sys.argv[1])
st = sys.argv[2]
d = st.find("day")
if d == -1:
    one_time = int(st)
    times = ceil(total_page / one_time)
else:
    times = int(st[:d])
    one_time = total_page // times

order = list(range(0, times))
random.shuffle(order)

with open(output, "w") as f:
    for pg in order:
        if pg == times - 1:
            final_page = total_page
        else:
            final_page = (pg + 1) * one_time
        string = str(pg * one_time + 1) + "~" + str(final_page) + "\n"
        f.write(string)
