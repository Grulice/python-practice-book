# Problem 70: Write a program csv2xls.py that reads a csv file and exports it as Excel file. The program should
# take two arguments. The name of the csv file to read as first argument and the name of the Excel file to write as
# the second argument.

import sys
import tablib

# try to get the file names from argv, switch to default if none provided
try:
    CSV_PATH = sys.argv[1]
    XLS_PATH = sys.argv[2]
except IndexError as err:
    print(err)
    print("CSV or Excel path not provided; using defaults...")
    CSV_PATH = './assets/CommaSeparated.csv'
    XLS_PATH = './assets/CommaSeparated_EXCEL.xls'

data = tablib.Dataset()  # create the tablib table

with open(CSV_PATH, 'r') as f:
    csv_lines = f.readlines()  # read contents of csv file into a list

for line in csv_lines:
    data.append(line.split(','))  # add the rows to the tablib table as lists

with open(XLS_PATH, 'wb') as f:  # data.export() returns a byte stream, file must be opened in 'wb' mode (write bytes)
    f.write(data.export('xls'))  # export tablib table to xls and write to file
