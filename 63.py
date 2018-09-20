"""Problem 63: Write a program antihtml.py that takes a URL as argument,
downloads the html from web and print it after stripping html tags."""

import urllib.request
import os
import sys
import re



# if no argument is provided - URL is set to bbc.com's home page
try:
    URL = sys.argv[1]
except IndexError:
    URL = 'http://www.bbc.com/'


response = urllib.request.urlopen(URL)

urlPath = urllib.request.urlparse(URL)[2]  # strip everything up to and incl. 1 lvl domain and params
file = lambda: urlPath.split('/')[-1] if urlPath.split('/')[-1] != '' else 'index.html'  # return basename