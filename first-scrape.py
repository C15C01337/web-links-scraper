#worked
#importing the required libraries

import requests
from bs4 import BeautifulSoup
import sys

# url = input("enter a url: ")

url = "https://hackasec.wordpress.com"

# step 1: get the page

r = requests.get(url)
htmlContent = r.content


# step 2: parse the page
soup = BeautifulSoup(htmlContent, 'html.parser')


# step 3: extract the data html tree traversal and find a links and save it to a file

file_path = 'links.txt'
sys.stdout = open(file_path, "w+")
for a in soup.find_all('a', href=True):
    link=a['href']
    
    print(link)

