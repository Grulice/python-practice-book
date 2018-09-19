"""Problem 63: Write a program antihtml.py that takes a URL as argument, downloads the html from web and print
it after stripping html tags."""

import urllib.request
import os
import sys
import re

# if no argument is provided - URL is set to bbc.com's home page
try:
    URL = sys.argv[1]
except IndexError:
    URL = 'http://www.bbc.com'


response = urllib.request.urlopen(URL)  # open the url
htmlstr = response.read().decode('utf-8')
# response.read() returns the contents of the page
# however, it returns it as a byte array
# using decode() method we convert it into a string with the utf-8 encoding

pattern = re.compile(r'<\s*[^>]*>')  # set the regex to be used to find the HTML tags
print(pattern.sub(r'', htmlstr))  # pattern.sub(repl, str) replaces all occurrences of the pattern in str with repl

