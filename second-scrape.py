#worked
#importing the required libraries

import requests
from bs4 import BeautifulSoup
import sys

# url = input("enter a url: ")


#open the file and write the links to an list
urled = []
with open ('re-filter.txt', 'r') as file:
    for urlline in file:
        urlline = urlline.strip()
        urled.append(urlline)

# loop an list urled and scrape the links and append in a new file
for c in range(len(urled)):
    url = urled[c]

    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')

    file_path = 'ultimate-links.txt'
    sys.stdout = open(file_path, "a+")
    for a in soup.find_all('a', href=True):
        link=a['href']
        print(link)

