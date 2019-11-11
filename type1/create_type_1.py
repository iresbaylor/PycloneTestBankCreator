import ast
import pprint


def create_type_1(filename):
    tree = ast.parse(filename)
    pprint.pprint(tree)

    return tree