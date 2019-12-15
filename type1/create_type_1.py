import os
import random


def create_type_1(filename):
    if not os.path.exists('type1clones'):
        print('Creating type1clones directory...')
        os.mkdir('type1clones')
    with open(filename) as fp:
        print('original file name: ' + filename)
        newfilename = os.path.splitext(filename)[0]
        newfilename = 'type1clones/' + newfilename + str(random.randint(0, 10000)) + '.py'
        with open((newfilename), 'w') as fw:
            print('printing clone of ' + filename + ' to: type1clones/' + newfilename + '.py')
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
            print('finished printing clone of ' + filename + ' to: type1clones/' + newfilename + '.py')
