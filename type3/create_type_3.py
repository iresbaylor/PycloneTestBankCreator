import ast
import pprint
from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP


def create_type_3(filename):
    # open file
    file = open(filename, "r")

    # variables and stuff
    found = 0
    blank_line_count = 0
    str = ""

    nodes = []  # to hold all the ast for each function???

    # parse to find def in file
    for line in file:
        index = line.find('def')
        if index == 0 and found == 0:
            # found a function definition
            str = str+line
            found = 1
        elif found == 1:
            # check if blank line (to determine end of function)
            if line.isspace():
                blank_line_count = blank_line_count+1
            else:
                blank_line_count = 0
                # add to string of the whole function thing
                str = str+line

        if blank_line_count == 2:
            # finished with a function, make an ast of it
            # print(str)
            p = ast.parse(str)
            print(ast.dump(p))
            str = ""

    # close file
    file.close()