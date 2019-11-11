from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
import ast
import pprint


def create_type_3(filename):
    tree = ast.parse(filename)
    pprint.pprint(tree)

    return tree