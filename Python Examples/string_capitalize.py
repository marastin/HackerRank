#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    names = s.split(' ')
    for idx, name in enumerate(names):
        if len(name) > 1:
            names[idx] = name[0].upper() + name[1:]
        elif len(name) == 1:
            names[idx] = name[0].upper()
    return ' '.join(names)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
