from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
import ast
import pprint


def create_type_2(filename):
    # with open(filename, 'rb') as fp:
    #     # line = fp.readline()
    #     cnt = 1
    #     for ft in tokenize(fp.readline):
    #         print("Line {}".format(cnt))
    #         print("   {}".format(ft.type))
    #         print("   {}".format(ft.string))
    #         print("   {}".format(ft.start))
    #         print("   {}".format(ft.end))
    #         print("   {}".format(ft.line))
    #         # line = fp.readline()
    #         cnt += 1
    #
    # # out_file = open("t2Out.txt", "w")

    tree = ast.parse(filename)
    pprint.pprint(tree)

    return tree
