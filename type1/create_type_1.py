import os
import random


def create_type_1(filename):
    os.mkdir("/type1")
    with open(filename) as fp:
        with open(("type1/" + filename + random.randint(0, 100000)), 'w') as fw:
            line = fp.readline()
            line = line.strip()
            random.randint(1, 5)
            if random.randint(1, 5) == 1:
                fw.write("\n")
            if not line.startswith('#'):
                fw.write(line)
