#worked

import requests
from bs4 import BeautifulSoup
import sys

#open a social.txt file and write the links to an array

responseList = []
with open ('social.txt', 'r') as file:
    for resline in file:
        resline = resline.strip()
        responseList.append(resline)
#created two lists to store the links

broken = []
noice = []

# to get the status code and save it in a separte file
x = len(responseList)
print(x)
for a in range(x):
    req = requests.get(responseList[a])
    hello = req.status_code

    if hello == 200:
        print("200 okey")
        print(responseList[a])
        noice.append(responseList[a])
        
    else:
        print("404 error")
        print(responseList[a])
        broken.append(responseList[a])        



# open a file broken.txt and write an broken link        
file_paths = 'broken.txt'
sys.stdout = open(file_paths, "w+")
for b in range(len(broken)):
    print(broken[b])

# open a file noice.txt and write an noice link
file_pathss = 'noice.txt'
sys.stdout = open(file_pathss, "w+")
for c in range(len(noice)):
    print(noice[c])




