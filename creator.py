import ast
import sys
from sys import argv

from analyzer import Analyzer
from type1 import create_type_1 as type1
from type2 import create_type_2 as type2
from type3 import create_type_3 as type3


def main():
    if len(argv) < 2:
        print('you must pass at least one python filename to the script')
        exit(-1)

    i = 1
    while i < len(sys.argv):
        print("\nSTART OF TYPE 1 ------------------------")
        type1.create_type_1(argv[i])
        print("END OF TYPE 1 --------------------------\n")
        print("\nSTART OF TYPE 2 ------------------------")
        #type2.create_type_2(argv[i])
        print("END OF TYPE 2 --------------------------\n")
        print("\nSTART OF TYPE 3 ------------------------")
        # type3.create_type_3(argv[i])
        print("END OF TYPE 3 --------------------------\n")
        i = i+1
        print()

    # files = argv[1:]
    # for file in files:
    #     try:
    #         with open(file) as f:
    #             source = f.read()
    #         valid = True
    #         try:
    #             tree = ast.parse(source)
    #         except SyntaxError:
    #             print('you have passed an invalid python file named {}. check its syntax.\n'.format(file))
    #             valid = False
    #         if valid:
    #             analyzer = Analyzer()
    #             analyzer.visit(tree)
    #             analyzer.report(file)
    #     except FileNotFoundError:
    #         print('you have passed an invalid file: {}.\n'.format(file))


if __name__ == '__main__':
    main()
