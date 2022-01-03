#worked

import re
import sys

# open links.txt and write the links in a file
refilter = []
with open ('links.txt', 'r') as file:
    for line in file:
        line = line.strip()
        refilter.append(line)
        
# used regex for filtering the links with facebook and twitter

r = re.compile("https://+.*")
filtered_list = list(filter(r.match, refilter))

# print(filtered_list)

test_list = list(set(filtered_list))
# print(test_list)

file_path = 're-filter.txt'
sys.stdout = open(file_path, "w+")
for a in range(len(test_list)):
    print(test_list[a])
    