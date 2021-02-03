import sys
from sys import argv
import os

from logic import create_type_1 as type1, create_type_2 as type2, create_type_3 as type3

# Output directory for all files
_OUTPUT_DIR = 'output'
_TYPE_1_OUTPUT_DIR = 'type1'
_TYPE_2_OUTPUT_DIR = 'type2'
_TYPE_3_OUTPUT_DIR = 'type3'


def main():
    if len(argv) < 2:
        print('you must pass at least one python filename to the script')
        exit(-1)

    # Create output directory if it doesn't exist
    type1_output_path = os.path.join(_OUTPUT_DIR, _TYPE_1_OUTPUT_DIR)
    type2_output_path = os.path.join(_OUTPUT_DIR, _TYPE_2_OUTPUT_DIR)
    type3_output_path = os.path.join(_OUTPUT_DIR, _TYPE_3_OUTPUT_DIR)
    if not os.path.exists(_OUTPUT_DIR):
        os.makedirs(_OUTPUT_DIR)
        os.makedirs(type1_output_path)
        os.makedirs(type2_output_path)
        os.makedirs(type3_output_path)

    i = 1
    while i < len(sys.argv):
        print("\nSTART OF TYPE 1 ------------------------")
        type1.create_type_1(argv[i], type1_output_path)
        print("END OF TYPE 1 --------------------------\n")
        print("\nSTART OF TYPE 2 ------------------------")
        type2.create_type_2(argv[i], type2_output_path)
        print("END OF TYPE 2 --------------------------\n")
        print("\nSTART OF TYPE 3 ------------------------")
        type3.create_type_3(argv[i], type3_output_path)
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
