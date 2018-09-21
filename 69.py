# Problem 69: Write a program mydoc.py to implement the functionality of pydoc. The program should take
# the module name as argument and print documentation for the module and each of the functions defined in that
# module.
# Hints:
# • The dir function to get all entries of a module
# • The inspect.isfunction function can be used to test if given object is a function
# • x.__doc__ gives the docstring for x.
# • The __import__ function can be used to import a module by name

import sys
import inspect

# try to get the module name from argv, default to 'os' if none provided
try:
    MODULE_NAME = sys.argv[1]
except IndexError:
    MODULE_NAME = 'os'

module = __import__(MODULE_NAME)  # store the module object

# -- FLUFF-------------------------------------
print("Help on module {}".format(MODULE_NAME))
print("---------------------------------------------")
print("DESCRIPTION")
print("---------------------------------------------")
print("\n{}\n".format(module.__doc__))
print("---------------------------------------------")
print("FUNCTIONS")
print("---------------------------------------------")
# -- END FLUFF--------------------------------

# module.__dict__ contains names of attributes as keys and attribute objects themselves as values
for fname, funct in module.__dict__.items():  # get tuple of function name, function object from module
    if inspect.isfunction(funct):  # check if the current object is a function. Print docs if yes
        print(fname)
        print(funct.__doc__)
