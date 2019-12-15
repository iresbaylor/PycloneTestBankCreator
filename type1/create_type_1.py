import os
import random


def create_type_1(filename):
    os.mkdir("/type1")
    with open(filename) as fp:
        newfilename = os.path.splitext(filename[0])[0]
        with open(("type1/" + newfilename + random.randint(0, 10000) + '.py'), 'w') as fw:
            line = fp.readline()
            line = line.strip()
            random.randint(1, 5)
            if random.randint(1, 5) == 1:
                fw.write("\n")
            if not line.startswith('#'):
                fw.write(line)
