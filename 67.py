# Problem 67: Write a program myip.py to print the external IP address of the machine. Use the response
# from http://httpbin.org/get and read the IP address from there. The program should print only the
# IP address and nothing else.

import re
import json
import urllib.request


def getExtIP():
    response = urllib.request.urlopen('http://httpbin.org/get')  # open json url
    jsonstring = response.read().decode('utf-8')  # dump json file into string
    jsondict = json.loads(jsonstring)  # deserialize json string into a dictionary
    return jsondict['origin']  # get the value of the external IP from the response


print(getExtIP())
