"""Problem 62: Write a program wget.py to download a given URL. The program should accept a URL as argument, download
it and save it with the basename of the URL. If the URL ends with a /, consider the basename as index.html."""

import urllib.request
import os
import sys



# if no argument is provided - URL is set to bbc.com's home page
try:
    URL = sys.argv[1]
except IndexError:
    URL = 'http://www.gutenberg.org/ebooks/18187.epub.images?session_id=9cda2342e1645276ff7060f3778bc85c3295ff18'


urlPath = urllib.request.urlparse(URL)[2]  # strip everything up to and incl. 1 lvl domain and params
file = lambda: urlPath.split('/')[-1] if urlPath.split('/')[-1] != '' else 'index.html'  # return basename
urllib.request.urlretrieve(url=URL, filename=file())
