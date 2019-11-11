import ast
from sys import argv

from analyzer import Analyzer
from type2 import create_type_2 as type2

def main():
    if len(argv) < 2:
        print('you must pass at least one python filename to the script')
        exit(-1)
    type2.create_type_2(argv[1])
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
