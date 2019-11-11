import ast
import pprint
from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP


def create_type_3(filename):
    # open file
    file = open(filename, "r")

    found = 0
    blank_line_count = 0
    str = ""

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
            print(str)
            str = ""


    # # read from file line by line
    # # create ast based off line???
    # for line in file:
    #     print(line)
    #     try:
    #         p = ast.parse(line)
    #         print("parsed the thing")
    #         # check the nodes for things???
    #         for node in p.body:
    #             pprint.pprint(node)
    #     except:
    #         print("that stupid error on ", line)
    #

    # close file
    file.close()