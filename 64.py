"""Problem 64: Write a function make_slug that takes a name converts it into a slug. A slug is a string where spaces
and special characters are replaced by a hyphen, typically used to create blog post URL from post title. It should
also make sure there are no more than one hyphen in any place and there are no hyphens at the beginning and end
of the slug."""

import urllib.request
import os
import sys
import re


def make_slug(instring):
    start_end_pattern = re.compile(r'(^\W*|\W*$)')  # pattern for special chars at the start and end of string
    pattern = re.compile(r'\W+')  # pattern for all special chars in the string

    result = start_end_pattern.sub(r'', instring)  # remove special chars at the beginning and the end
    result = pattern.sub(r'-', result)  # replace special chars with a hyphen
    return result


print(make_slug(" --hello- world-123333                         333312412-412412-----------231451252315-"))