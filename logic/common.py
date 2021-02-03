import os
import random


def construct_output_file(filename, output_path):
    newfilename = os.path.splitext(filename)[0]
    newfilename = os.path.join(output_path, newfilename + str(random.randint(0, 10000)) + '.py')
    newdir = os.path.dirname(newfilename)
    if not os.path.exists(newdir):
        os.makedirs(newdir)
    return newfilename
