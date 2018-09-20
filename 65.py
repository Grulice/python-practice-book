"""Problem 65: Write a program links.py that takes URL of a webpage as argument
and prints all the URLs linked from that webpage."""

import urllib.request
import os
import sys
import re



# if no argument is provided - URL is set to bbc.com's home page
try:
    URL = sys.argv[1]
except IndexError:
    URL = 'http://www.bbc.com/'


response = urllib.request.urlopen(URL)  # open URL

htmlString = response.read().decode('utf-8')  # get the contents of the page as bytes, then convert to utf-8 string

pattern = re.compile(r'https?://(\w+\.*)+(/?[^"\'\n]+)*')  # regexp to find full URL's from the page's html code

matchIter = pattern.finditer(htmlString)  # get iterator over matches in the string

for match in enumerate(matchIter):  # enumerate the iterator to display the match number
    print("{0} -- {1}".format(match[0], match[1].group(0)))
