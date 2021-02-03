import os
import random

from logic.common import construct_output_file


def create_type_1(filename, output_path):
    with open(filename) as fp:
        print('original file name: ' + filename)
        print(os.path.splitext(filename))

        # Construct the output file
        new_filename = construct_output_file(filename, output_path)

        with open(new_filename, 'w') as fw:
            print('printing clone of ' + filename + ' to: ' + new_filename)
            line = fp.readline()
            linenumber = 1
            newlinenumber = 1
            while line:
                random.randint(1, 5)
                if random.randint(1, 5) == 1:
                    print('Adding a newline at line #: ' + str(newlinenumber))
                    newlinenumber += 1
                    fw.write("\n")
                if not line.strip().startswith('#'):
                    fw.write(line)
                else:
                    print('Stripping in-line comment line #: ' + str(linenumber))
                line = fp.readline()
                newlinenumber += 1
                linenumber += 1
            print('finished printing clone of ' + filename + ' to: type1clones/' + new_filename + '.py')
