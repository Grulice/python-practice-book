# Problem 71: Create a new virtualenv and install BeautifulSoup. BeautifulSoup is very good library for parsing
# HTML. Try using it to extract all HTML links from a webpage.

import sys
import tablib
import urllib.request
from bs4 import BeautifulSoup


response = urllib.request.urlopen('http://www.bbc.com')
htmlString = response.read()

soup = BeautifulSoup(htmlString, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))