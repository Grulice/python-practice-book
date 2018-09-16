"""Problem 49: Write a python function parse_csv to parse csv (comma separated values) files."""


# constants
file_path = "CommaSeparated_CustomDelim.csv"


def csv_parse(input_file, delimiter_char=',', comment_char='#'):
    file_lines = input_file.readlines()
    return [x.strip().split(delimiter_char) for x in file_lines if x[0] != comment_char]


# open file
try:
    file = open(file_path, 'r')
except FileNotFoundError as err:
    print(err)

print(csv_parse(file, '!'))
