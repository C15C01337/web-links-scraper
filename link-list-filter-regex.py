#worked

import re
import sys

# open links.txt and write the links in a file
listed = []
with open ('ultimate-links.txt', 'r') as file:
    for line in file:
        line = line.strip()
        listed.append(line)
        
# used regex for filtering the links with facebook and twitter

r = re.compile("https+://+www+.[{f}{t}{g}{i}].+")
filtered_list = list(filter(r.match, listed))

print(filtered_list)
test_list = list(set(filtered_list))

file_path = 'social.txt'
sys.stdout = open(file_path, "w+")
for a in range(len(test_list)):
    print(test_list[a])
    







