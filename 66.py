# Problem 66: Write a regular expression to validate a phone number.

import re


def isPhoneNum(instring):
    pattern = re.match(r'\+?\d{1,3}\(?\d{1,3}\)?\s?\d{3}-?\d{2}-?\d{2}', instring)
    if pattern is not None and pattern.group(0) == instring:  # re.match() returns None if no matches are found
        return True
    else:
        return False


print(isPhoneNum('+123456789'))
