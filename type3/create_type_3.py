from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
import ast
import pprint


def create_type_3(filename):
    # open file
    file = open(filename, "r")

    # read from file line by line
    # create ast based off line???
    for line in file:
        print(line)
        try:
            p = ast.parse(line)
            print("parsed the thing")
            # check the nodes for things???
            for node in p.body:
                pprint.pprint(node)
        except:
            print("that stupid error on ", line)

    # close file
    file.close()