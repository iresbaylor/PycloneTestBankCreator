import os
import random


def create_type_1(filename):
    os.mkdir("/type1")
    with open(filename) as fp:
        with open(("type1/" + filename + random.randint(0, 100000)), 'w') as fw:
            line = fp.readline()
            random.randint(1, 5)
            if random.randint(1, 5) == 1:
                fw.write("\n")
            fw.write(line)
